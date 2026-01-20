#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Semantic Scholar API Fetcher
Fetches citation data and related papers from Semantic Scholar
"""

import sys
import io
import os
import requests
import json
from pathlib import Path
from typing import Dict, List, Optional
import time

# Fix Windows console encoding issue
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


class SemanticScholarFetcher:
    """Fetcher for Semantic Scholar API"""

    BASE_URL = "https://api.semanticscholar.org/graph/v1"

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize fetcher with optional API key

        Args:
            api_key: Semantic Scholar API key (optional, for higher rate limits)
        """
        self.api_key = api_key or os.getenv("SEMANTIC_SCHOLAR_API_KEY")
        self.headers = {}
        if self.api_key:
            self.headers["x-api-key"] = self.api_key

    def fetch_paper_data(self, arxiv_id: str) -> Optional[Dict]:
        """
        Fetch paper data from Semantic Scholar

        Args:
            arxiv_id: arXiv ID (e.g., "2401.12345")

        Returns:
            Dictionary with paper data or None if failed
        """
        # Clean arxiv_id
        arxiv_id = arxiv_id.replace("arxiv:", "").replace("arXiv:", "").strip()

        # Build API URL
        url = f"{self.BASE_URL}/paper/arXiv:{arxiv_id}"

        # Request fields
        fields = [
            "paperId",
            "title",
            "abstract",
            "year",
            "citationCount",
            "referenceCount",
            "influentialCitationCount",
            "citations",
            "citations.title",
            "citations.year",
            "citations.citationCount",
            "references",
            "references.title",
            "references.year",
            "references.citationCount",
            "externalIds",
            "url"
        ]

        params = {"fields": ",".join(fields)}

        try:
            response = requests.get(
                url,
                headers=self.headers,
                params=params,
                timeout=30
            )

            if response.status_code == 404:
                print(f"Paper {arxiv_id} not found in Semantic Scholar")
                print("This is normal for very recent papers")
                return None

            if response.status_code == 429:
                print("Rate limit exceeded")
                if not self.api_key:
                    print("Consider getting an API key from https://www.semanticscholar.org/product/api")
                return None

            response.raise_for_status()

            data = response.json()

            # Extract relevant information
            paper_data = {
                "paper_id": data.get("paperId"),
                "title": data.get("title"),
                "abstract": data.get("abstract"),
                "year": data.get("year"),
                "citation_count": data.get("citationCount", 0),
                "reference_count": data.get("referenceCount", 0),
                "influential_citation_count": data.get("influentialCitationCount", 0),
                "url": data.get("url"),
                "external_ids": data.get("externalIds", {}),
                "citations": self._extract_paper_list(data.get("citations", []), limit=10),
                "references": self._extract_paper_list(data.get("references", []), limit=10)
            }

            return paper_data

        except requests.RequestException as e:
            print(f"Error fetching from Semantic Scholar: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON response: {e}")
            return None

    def _extract_paper_list(self, papers: List[Dict], limit: int = 10) -> List[Dict]:
        """
        Extract simplified paper information from list

        Args:
            papers: List of paper dictionaries
            limit: Maximum number of papers to return

        Returns:
            List of simplified paper dictionaries
        """
        result = []
        for paper in papers[:limit]:
            result.append({
                "title": paper.get("title", "Unknown"),
                "year": paper.get("year"),
                "citation_count": paper.get("citationCount", 0)
            })
        return result

    def search_papers(self, query: str, limit: int = 10) -> List[Dict]:
        """
        Search papers by query

        Args:
            query: Search query
            limit: Maximum number of results

        Returns:
            List of paper dictionaries
        """
        url = f"{self.BASE_URL}/paper/search"
        params = {
            "query": query,
            "limit": limit,
            "fields": "paperId,title,abstract,year,citationCount,authors"
        }

        try:
            response = requests.get(
                url,
                headers=self.headers,
                params=params,
                timeout=30
            )
            response.raise_for_status()

            data = response.json()
            return data.get("data", [])

        except requests.RequestException as e:
            print(f"Error searching papers: {e}")
            return []

    def get_related_papers(self, arxiv_id: str, limit: int = 5) -> List[Dict]:
        """
        Get papers related to the given arXiv paper

        Args:
            arxiv_id: arXiv ID
            limit: Maximum number of related papers

        Returns:
            List of related paper dictionaries
        """
        arxiv_id = arxiv_id.replace("arxiv:", "").replace("arXiv:", "").strip()

        # First get the paper data
        paper_data = self.fetch_paper_data(arxiv_id)
        if not paper_data:
            return []

        # Combine citations and references, sort by citation count
        all_related = paper_data["citations"] + paper_data["references"]
        all_related.sort(key=lambda p: p.get("citation_count", 0), reverse=True)

        return all_related[:limit]

    def check_api_status(self) -> Dict:
        """
        Check API status and rate limits

        Returns:
            Dictionary with API status information
        """
        # Make a simple request to check status
        url = f"{self.BASE_URL}/paper/arXiv:2401.00001"  # Use a known paper
        params = {"fields": "paperId"}

        try:
            response = requests.get(
                url,
                headers=self.headers,
                params=params,
                timeout=10
            )

            status = {
                "available": response.status_code != 503,
                "has_api_key": bool(self.api_key),
                "rate_limit": "5000 requests per 5 minutes" if self.api_key else "100 requests per 5 minutes",
                "status_code": response.status_code
            }

            return status

        except requests.RequestException as e:
            return {
                "available": False,
                "has_api_key": bool(self.api_key),
                "error": str(e)
            }


def main():
    """Command-line interface"""
    import argparse

    parser = argparse.ArgumentParser(description="Fetch citation data from Semantic Scholar")
    parser.add_argument("arxiv_id", help="arXiv ID (e.g., 2401.12345)")
    parser.add_argument("--api-key", help="Semantic Scholar API key (optional)")
    parser.add_argument("--output", help="Output JSON file path (optional)")
    parser.add_argument("--check-status", action="store_true", help="Check API status")

    args = parser.parse_args()

    fetcher = SemanticScholarFetcher(api_key=args.api_key)

    if args.check_status:
        status = fetcher.check_api_status()
        print("\n=== Semantic Scholar API Status ===")
        print(json.dumps(status, indent=2))
        return

    # Fetch paper data
    print(f"Fetching data for arXiv:{args.arxiv_id}...")
    paper_data = fetcher.fetch_paper_data(args.arxiv_id)

    if paper_data:
        print("\n=== Paper Data ===")
        print(f"Title: {paper_data['title']}")
        print(f"Year: {paper_data['year']}")
        print(f"Citation Count: {paper_data['citation_count']}")
        print(f"Reference Count: {paper_data['reference_count']}")
        print(f"Influential Citations: {paper_data['influential_citation_count']}")

        print(f"\n=== Top Citations ({len(paper_data['citations'])}) ===")
        for i, citation in enumerate(paper_data['citations'][:5], 1):
            print(f"{i}. {citation['title']} ({citation['year']}) - {citation['citation_count']} citations")

        print(f"\n=== Top References ({len(paper_data['references'])}) ===")
        for i, reference in enumerate(paper_data['references'][:5], 1):
            print(f"{i}. {reference['title']} ({reference['year']}) - {reference['citation_count']} citations")

        # Save to file if requested
        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(paper_data, f, indent=2, ensure_ascii=False)
            print(f"\n✓ Data saved to: {output_path}")
    else:
        print("Failed to fetch paper data")
        sys.exit(1)


if __name__ == "__main__":
    main()
