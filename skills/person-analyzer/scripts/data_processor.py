"""
Data processor for person-analyzer skill.
Handles data validation, credibility scoring, and cross-validation.
"""

import json
from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path


class DataProcessor:
    """Process and validate biographical data."""

    def __init__(self):
        """Initialize data processor."""
        self.source_credibility_map = {
            "official_website": 100,
            "verified_interview": 100,
            "autobiography": 100,
            "wikipedia": 80,
            "major_news": 80,
            "academic_profile": 80,
            "linkedin": 75,
            "blog": 60,
            "social_media_verified": 60,
            "industry_publication": 60,
            "social_media": 40,
            "forum": 40,
            "unknown": 30,
        }

    def calculate_source_credibility(self, source_type: str, url: str = "") -> int:
        """
        Calculate credibility score for a source.

        Args:
            source_type: Type of source
            url: Source URL (optional, for additional validation)

        Returns:
            Credibility score (0-100)
        """
        base_score = self.source_credibility_map.get(
            source_type.lower(), self.source_credibility_map["unknown"]
        )

        # Adjust based on URL patterns
        if url:
            url_lower = url.lower()
            if any(
                domain in url_lower
                for domain in [
                    "wikipedia.org",
                    "britannica.com",
                    "biography.com",
                ]
            ):
                base_score = max(base_score, 80)
            elif any(
                domain in url_lower
                for domain in [
                    "nytimes.com",
                    "wsj.com",
                    "ft.com",
                    "economist.com",
                ]
            ):
                base_score = max(base_score, 85)
            elif any(
                domain in url_lower
                for domain in ["linkedin.com", "crunchbase.com"]
            ):
                base_score = max(base_score, 75)

        return base_score

    def cross_validate_fact(
        self, fact: str, sources: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Cross-validate a fact from multiple sources.

        Args:
            fact: The fact to validate
            sources: List of sources containing the fact

        Returns:
            Validation result with credibility score
        """
        if len(sources) == 0:
            return {
                "fact": fact,
                "validated": False,
                "credibility": 0,
                "sources_count": 0,
                "status": "no_sources",
            }

        if len(sources) == 1:
            return {
                "fact": fact,
                "validated": False,
                "credibility": sources[0].get("credibility", 50),
                "sources_count": 1,
                "status": "single_source",
            }

        # Multiple sources - calculate weighted credibility
        total_credibility = sum(s.get("credibility", 50) for s in sources)
        avg_credibility = total_credibility / len(sources)

        # Boost credibility if multiple high-quality sources agree
        if len(sources) >= 3 and avg_credibility >= 70:
            avg_credibility = min(avg_credibility * 1.1, 100)

        return {
            "fact": fact,
            "validated": True,
            "credibility": round(avg_credibility, 1),
            "sources_count": len(sources),
            "status": "validated",
        }

    def detect_conflicts(
        self, dimension_data: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """
        Detect conflicts in dimensional data.

        Args:
            dimension_data: Data for a specific dimension

        Returns:
            List of detected conflicts
        """
        conflicts = []

        # Check for date conflicts
        if "dates" in dimension_data:
            dates = dimension_data["dates"]
            if isinstance(dates, list) and len(dates) > 1:
                # Check for inconsistent dates
                unique_dates = set(d["value"] for d in dates if "value" in d)
                if len(unique_dates) > 1:
                    conflicts.append(
                        {
                            "type": "date_conflict",
                            "field": "dates",
                            "values": list(unique_dates),
                            "sources": [d.get("source") for d in dates],
                        }
                    )

        # Check for factual conflicts
        if "facts" in dimension_data:
            facts = dimension_data["facts"]
            # Group facts by topic
            fact_groups = {}
            for fact in facts:
                topic = fact.get("topic", "general")
                if topic not in fact_groups:
                    fact_groups[topic] = []
                fact_groups[topic].append(fact)

            # Check for conflicts within each topic
            for topic, topic_facts in fact_groups.items():
                if len(topic_facts) > 1:
                    # Simple conflict detection: different values for same topic
                    values = [f.get("value") for f in topic_facts]
                    if len(set(str(v) for v in values)) > 1:
                        conflicts.append(
                            {
                                "type": "factual_conflict",
                                "topic": topic,
                                "values": values,
                                "sources": [f.get("source") for f in topic_facts],
                            }
                        )

        return conflicts

    def calculate_dimension_credibility(
        self, dimension_data: Dict[str, Any]
    ) -> float:
        """
        Calculate overall credibility for a dimension.

        Args:
            dimension_data: Data for a specific dimension

        Returns:
            Credibility score (0-100)
        """
        if not dimension_data:
            return 0.0

        sources = dimension_data.get("sources", [])
        if not sources:
            return 30.0  # Low credibility if no sources

        # Calculate average source credibility
        credibilities = [s.get("credibility", 50) for s in sources]
        avg_credibility = sum(credibilities) / len(credibilities)

        # Adjust based on number of sources
        if len(sources) >= 5:
            avg_credibility = min(avg_credibility * 1.1, 100)
        elif len(sources) >= 3:
            avg_credibility = min(avg_credibility * 1.05, 100)

        # Penalize if conflicts detected
        conflicts = dimension_data.get("conflicts", [])
        if conflicts:
            penalty = min(len(conflicts) * 5, 20)
            avg_credibility = max(avg_credibility - penalty, 40)

        return round(avg_credibility, 1)

    def calculate_overall_credibility(
        self, all_dimensions: Dict[str, Dict[str, Any]]
    ) -> float:
        """
        Calculate overall credibility across all dimensions.

        Args:
            all_dimensions: Data for all dimensions

        Returns:
            Overall credibility score (0-100)
        """
        dimension_scores = []

        for dimension_name, dimension_data in all_dimensions.items():
            score = self.calculate_dimension_credibility(dimension_data)
            dimension_scores.append(score)

        if not dimension_scores:
            return 0.0

        return round(sum(dimension_scores) / len(dimension_scores), 1)

    def normalize_person_name(self, name: str) -> Dict[str, str]:
        """
        Normalize person name for consistent storage and search.

        Args:
            name: Person's name

        Returns:
            Dictionary with normalized forms
        """
        # Remove extra whitespace
        normalized = " ".join(name.split())

        # Create file-safe version
        file_safe = normalized.replace(" ", "_").replace("/", "_")

        # Detect if Chinese or English
        has_chinese = any("\u4e00" <= char <= "\u9fff" for char in normalized)

        return {
            "original": name,
            "normalized": normalized,
            "file_safe": file_safe,
            "language": "chinese" if has_chinese else "english",
        }

    def merge_duplicate_sources(
        self, sources: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Merge duplicate sources based on URL.

        Args:
            sources: List of sources

        Returns:
            Deduplicated list of sources
        """
        seen_urls = {}
        merged = []

        for source in sources:
            url = source.get("url", "")
            if not url:
                merged.append(source)
                continue

            if url in seen_urls:
                # Merge with existing source
                existing = seen_urls[url]
                # Keep higher credibility
                if source.get("credibility", 0) > existing.get("credibility", 0):
                    existing["credibility"] = source["credibility"]
                # Merge facts
                if "facts" in source:
                    if "facts" not in existing:
                        existing["facts"] = []
                    existing["facts"].extend(source["facts"])
            else:
                seen_urls[url] = source
                merged.append(source)

        return merged

    def save_dimension_data(
        self,
        person_data_dir: Path,
        dimension_name: str,
        dimension_data: Dict[str, Any],
    ):
        """
        Save dimension data to file.

        Args:
            person_data_dir: Person's data directory
            dimension_name: Name of the dimension
            dimension_data: Data to save
        """
        dimensions_dir = person_data_dir / "dimensions"
        dimensions_dir.mkdir(exist_ok=True)

        file_path = dimensions_dir / f"{dimension_name}.json"
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(dimension_data, f, indent=2, ensure_ascii=False)

    def load_dimension_data(
        self, person_data_dir: Path, dimension_name: str
    ) -> Optional[Dict[str, Any]]:
        """
        Load dimension data from file.

        Args:
            person_data_dir: Person's data directory
            dimension_name: Name of the dimension

        Returns:
            Dimension data or None if not found
        """
        file_path = person_data_dir / "dimensions" / f"{dimension_name}.json"

        if not file_path.exists():
            return None

        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)


if __name__ == "__main__":
    # Test data processor
    processor = DataProcessor()

    # Test source credibility
    print("Source credibility tests:")
    print(
        f"  Wikipedia: {processor.calculate_source_credibility('wikipedia', 'https://en.wikipedia.org/wiki/Test')}"
    )
    print(
        f"  Major news: {processor.calculate_source_credibility('major_news', 'https://nytimes.com/article')}"
    )
    print(f"  Blog: {processor.calculate_source_credibility('blog', '')}")

    # Test cross-validation
    print("\nCross-validation test:")
    sources = [
        {"url": "source1.com", "credibility": 80},
        {"url": "source2.com", "credibility": 75},
        {"url": "source3.com", "credibility": 85},
    ]
    result = processor.cross_validate_fact("Test fact", sources)
    print(f"  Validated: {result['validated']}")
    print(f"  Credibility: {result['credibility']}")
    print(f"  Sources: {result['sources_count']}")
