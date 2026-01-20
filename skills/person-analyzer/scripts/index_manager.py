"""
Index and cache manager for person-analyzer skill.
Manages analysis history and cached search results.
"""

import json
from typing import Dict, Any, Optional, List
from pathlib import Path
from datetime import datetime, timedelta


class IndexManager:
    """Manage analysis index."""

    def __init__(self, skill_dir: Path):
        """
        Initialize index manager.

        Args:
            skill_dir: Path to person-analyzer skill directory
        """
        self.skill_dir = Path(skill_dir)
        self.index_path = self.skill_dir / "index.json"

    def load_index(self) -> Dict[str, Any]:
        """
        Load analysis index.

        Returns:
            Index data
        """
        if not self.index_path.exists():
            return {"analyses": [], "last_updated": None}

        with open(self.index_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_index(self, index_data: Dict[str, Any]):
        """
        Save analysis index.

        Args:
            index_data: Index data to save
        """
        with open(self.index_path, "w", encoding="utf-8") as f:
            json.dump(index_data, f, indent=2, ensure_ascii=False)

    def add_analysis(
        self,
        person_name: str,
        domain: str,
        depth: str,
        language: str,
        report_path: str,
        credibility_score: float,
        stats: Dict[str, Any],
    ) -> str:
        """
        Add new analysis to index.

        Args:
            person_name: Name of the person
            domain: Analysis domain
            depth: Analysis depth
            language: Report language
            report_path: Path to report file
            credibility_score: Overall credibility score
            stats: Analysis statistics

        Returns:
            Analysis ID
        """
        index = self.load_index()

        # Generate analysis ID
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        normalized_name = person_name.replace(" ", "_").replace("/", "_")
        analysis_id = f"{normalized_name}_{timestamp}"

        # Create analysis entry
        analysis_entry = {
            "id": analysis_id,
            "person_name": person_name,
            "domain": domain,
            "depth": depth,
            "language": language,
            "generated_at": datetime.now().isoformat(),
            "report_path": report_path,
            "credibility_score": credibility_score,
            "stats": stats,
        }

        # Add to index
        index["analyses"].append(analysis_entry)
        index["last_updated"] = datetime.now().isoformat()

        # Save index
        self.save_index(index)

        return analysis_id

    def find_analysis(
        self, person_name: str, domain: Optional[str] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Find existing analysis for a person.

        Args:
            person_name: Name of the person
            domain: Optional domain filter

        Returns:
            Analysis entry or None if not found
        """
        index = self.load_index()

        for analysis in reversed(index["analyses"]):  # Most recent first
            if analysis["person_name"].lower() == person_name.lower():
                if domain is None or analysis["domain"] == domain:
                    return analysis

        return None

    def list_analyses(
        self, domain: Optional[str] = None, limit: int = 10
    ) -> List[Dict[str, Any]]:
        """
        List recent analyses.

        Args:
            domain: Optional domain filter
            limit: Maximum number of results

        Returns:
            List of analysis entries
        """
        index = self.load_index()
        analyses = index["analyses"]

        # Filter by domain if specified
        if domain:
            analyses = [a for a in analyses if a["domain"] == domain]

        # Sort by date (most recent first)
        analyses.sort(key=lambda x: x["generated_at"], reverse=True)

        return analyses[:limit]

    def get_stats(self) -> Dict[str, Any]:
        """
        Get overall statistics.

        Returns:
            Statistics dictionary
        """
        index = self.load_index()
        analyses = index["analyses"]

        if not analyses:
            return {
                "total_analyses": 0,
                "domains": {},
                "avg_credibility": 0,
                "last_analysis": None,
            }

        # Calculate statistics
        domains = {}
        total_credibility = 0

        for analysis in analyses:
            domain = analysis["domain"]
            domains[domain] = domains.get(domain, 0) + 1
            total_credibility += analysis.get("credibility_score", 0)

        return {
            "total_analyses": len(analyses),
            "domains": domains,
            "avg_credibility": round(total_credibility / len(analyses), 1),
            "last_analysis": analyses[-1]["generated_at"],
        }


class CacheManager:
    """Manage cached search results."""

    def __init__(self, skill_dir: Path):
        """
        Initialize cache manager.

        Args:
            skill_dir: Path to person-analyzer skill directory
        """
        self.skill_dir = Path(skill_dir)
        self.cache_dir = self.skill_dir / "cache"
        self.cache_dir.mkdir(exist_ok=True)

    def get_cache_path(self, cache_key: str) -> Path:
        """
        Get cache file path for a key.

        Args:
            cache_key: Cache key

        Returns:
            Path to cache file
        """
        # Sanitize cache key for filename
        safe_key = cache_key.replace(" ", "_").replace("/", "_")
        return self.cache_dir / f"{safe_key}.json"

    def get_cache(self, cache_key: str, max_age_days: int = 30) -> Optional[Any]:
        """
        Get cached data if it exists and is not expired.

        Args:
            cache_key: Cache key
            max_age_days: Maximum age in days

        Returns:
            Cached data or None if not found or expired
        """
        cache_path = self.get_cache_path(cache_key)

        if not cache_path.exists():
            return None

        # Check age
        mtime = datetime.fromtimestamp(cache_path.stat().st_mtime)
        age = datetime.now() - mtime

        if age > timedelta(days=max_age_days):
            # Cache expired
            cache_path.unlink()
            return None

        # Load cache
        with open(cache_path, "r", encoding="utf-8") as f:
            cache_data = json.load(f)

        return cache_data.get("data")

    def set_cache(self, cache_key: str, data: Any):
        """
        Set cached data.

        Args:
            cache_key: Cache key
            data: Data to cache
        """
        cache_path = self.get_cache_path(cache_key)

        cache_data = {
            "key": cache_key,
            "cached_at": datetime.now().isoformat(),
            "data": data,
        }

        with open(cache_path, "w", encoding="utf-8") as f:
            json.dump(cache_data, f, indent=2, ensure_ascii=False)

    def clean_expired_cache(self, max_age_days: int = 30) -> int:
        """
        Clean expired cache files.

        Args:
            max_age_days: Maximum age in days

        Returns:
            Number of files deleted
        """
        deleted_count = 0
        cutoff_time = datetime.now() - timedelta(days=max_age_days)

        for cache_file in self.cache_dir.glob("*.json"):
            mtime = datetime.fromtimestamp(cache_file.stat().st_mtime)

            if mtime < cutoff_time:
                cache_file.unlink()
                deleted_count += 1

        return deleted_count

    def clear_all_cache(self) -> int:
        """
        Clear all cache files.

        Returns:
            Number of files deleted
        """
        deleted_count = 0

        for cache_file in self.cache_dir.glob("*.json"):
            cache_file.unlink()
            deleted_count += 1

        return deleted_count


if __name__ == "__main__":
    # Test index and cache managers
    import sys

    if len(sys.argv) > 1:
        skill_dir = Path(sys.argv[1])
    else:
        skill_dir = Path(__file__).parent.parent

    # Test IndexManager
    print("Testing IndexManager...")
    index_manager = IndexManager(skill_dir)

    stats = index_manager.get_stats()
    print(f"  Total analyses: {stats['total_analyses']}")
    print(f"  Domains: {stats['domains']}")
    print(f"  Avg credibility: {stats['avg_credibility']}")

    # Test CacheManager
    print("\nTesting CacheManager...")
    cache_manager = CacheManager(skill_dir)

    # Test cache set/get
    test_key = "test_person_biography"
    test_data = {"name": "Test Person", "bio": "Test biography"}

    cache_manager.set_cache(test_key, test_data)
    cached = cache_manager.get_cache(test_key)

    if cached == test_data:
        print("  ✓ Cache set/get working")
    else:
        print("  ✗ Cache set/get failed")

    # Clean up test cache
    cache_manager.get_cache_path(test_key).unlink()
