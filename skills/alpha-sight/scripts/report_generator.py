#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Report Generator for Alpha-Sight
Generates analysis reports from templates
"""

import sys
import io
import os
import json
from pathlib import Path
from typing import Dict, Optional
from datetime import datetime

# Fix Windows console encoding issue
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


class ReportGenerator:
    """Generator for analysis reports"""

    def __init__(self, skill_path: Optional[str] = None):
        """
        Initialize report generator

        Args:
            skill_path: Path to alpha-sight skill directory
        """
        if skill_path is None:
            # Get the skill directory (parent of scripts directory)
            script_dir = Path(__file__).parent
            skill_path = script_dir.parent
        self.skill_path = Path(skill_path)
        self.assets_path = self.skill_path / "assets"

    def load_template(self, language: str = "english") -> str:
        """
        Load report template

        Args:
            language: Report language (english or chinese)

        Returns:
            Template content as string
        """
        if language == "chinese":
            template_file = self.assets_path / "report_template_zh.md"
        else:
            template_file = self.assets_path / "report_template_en.md"

        if not template_file.exists():
            raise FileNotFoundError(f"Template not found: {template_file}")

        with open(template_file, 'r', encoding='utf-8') as f:
            return f.read()

    def generate_report(
        self,
        arxiv_id: str,
        metadata: Dict,
        analysis: Optional[Dict] = None,
        reproduction: Optional[Dict] = None,
        citations: Optional[Dict] = None,
        language: str = "english",
        depth: str = "medium"
    ) -> str:
        """
        Generate report from template and data

        Args:
            arxiv_id: arXiv ID
            metadata: Paper metadata dictionary
            analysis: Analysis results dictionary (optional)
            reproduction: Reproduction results dictionary (optional)
            citations: Citation data dictionary (optional)
            language: Report language
            depth: Analysis depth

        Returns:
            Generated report content
        """
        # Load template
        template = self.load_template(language)

        # Prepare variables
        variables = self._prepare_variables(
            arxiv_id=arxiv_id,
            metadata=metadata,
            analysis=analysis,
            reproduction=reproduction,
            citations=citations,
            language=language,
            depth=depth
        )

        # Fill template
        report = self._fill_template(template, variables)

        return report

    def _prepare_variables(
        self,
        arxiv_id: str,
        metadata: Dict,
        analysis: Optional[Dict],
        reproduction: Optional[Dict],
        citations: Optional[Dict],
        language: str,
        depth: str
    ) -> Dict:
        """
        Prepare variables for template filling

        Args:
            arxiv_id: arXiv ID
            metadata: Paper metadata
            analysis: Analysis results
            reproduction: Reproduction results
            citations: Citation data
            language: Report language
            depth: Analysis depth

        Returns:
            Dictionary of template variables
        """
        variables = {
            # Basic info
            "Title": metadata.get("title", "Unknown"),
            "arxiv_id": arxiv_id,
            "published_date": metadata.get("published_date", "Unknown"),
            "authors": ", ".join(metadata.get("authors", [])),
            "categories": ", ".join(metadata.get("categories", [])),
            "project_homepage": metadata.get("project_homepage", "N/A"),

            # Abstract
            "one_sentence_summary": analysis.get("summary", "TBD") if analysis else "TBD",
            "original_abstract": metadata.get("abstract", ""),
            "abstract_in_chinese_if_needed": "",  # To be filled by Claude

            # Analysis
            "X": str(analysis.get("relevance_score", 0)) if analysis else "0",

            # Reproduction
            "status": reproduction.get("status", "not_attempted") if reproduction else "not_attempted",
            "method": reproduction.get("method", "none") if reproduction else "none",
            "URL": reproduction.get("repo_url", "not found") if reproduction else "not found",
            "N": str(reproduction.get("iterations", 0)) if reproduction else "0",

            # Citations
            "count": str(citations.get("citation_count", 0)) if citations else "0",
            "date": datetime.now().strftime("%Y-%m-%d"),

            # Tags
            "tags_list": ", ".join(metadata.get("tags", [])) if metadata.get("tags") else "TBD",

            # Meta
            "timestamp": datetime.now().isoformat(),
            "depth": depth
        }

        return variables

    def _fill_template(self, template: str, variables: Dict) -> str:
        """
        Fill template with variables

        Args:
            template: Template content
            variables: Dictionary of variables

        Returns:
            Filled template
        """
        result = template
        for key, value in variables.items():
            placeholder = "{" + key + "}"
            result = result.replace(placeholder, str(value))

        return result

    def save_report(self, report: str, output_path: str):
        """
        Save report to file

        Args:
            report: Report content
            output_path: Output file path
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report)

        print(f"✓ Report saved to: {output_path}")

    def generate_from_files(
        self,
        arxiv_id: str,
        metadata_file: Optional[str] = None,
        analysis_file: Optional[str] = None,
        reproduction_file: Optional[str] = None,
        citations_file: Optional[str] = None,
        language: str = "english",
        depth: str = "medium",
        output_file: Optional[str] = None
    ) -> str:
        """
        Generate report from JSON files

        Args:
            arxiv_id: arXiv ID
            metadata_file: Path to metadata JSON file
            analysis_file: Path to analysis JSON file (optional)
            reproduction_file: Path to reproduction JSON file (optional)
            citations_file: Path to citations JSON file (optional)
            language: Report language
            depth: Analysis depth
            output_file: Output file path (optional)

        Returns:
            Generated report content
        """
        # Load metadata
        if metadata_file:
            with open(metadata_file, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
        else:
            metadata = {"arxiv_id": arxiv_id}

        # Load optional files
        analysis = None
        if analysis_file and Path(analysis_file).exists():
            with open(analysis_file, 'r', encoding='utf-8') as f:
                analysis = json.load(f)

        reproduction = None
        if reproduction_file and Path(reproduction_file).exists():
            with open(reproduction_file, 'r', encoding='utf-8') as f:
                reproduction = json.load(f)

        citations = None
        if citations_file and Path(citations_file).exists():
            with open(citations_file, 'r', encoding='utf-8') as f:
                citations = json.load(f)

        # Generate report
        report = self.generate_report(
            arxiv_id=arxiv_id,
            metadata=metadata,
            analysis=analysis,
            reproduction=reproduction,
            citations=citations,
            language=language,
            depth=depth
        )

        # Save if output file specified
        if output_file:
            self.save_report(report, output_file)

        return report


def main():
    """Command-line interface"""
    import argparse

    parser = argparse.ArgumentParser(description="Generate analysis report from template")
    parser.add_argument("arxiv_id", help="arXiv ID (e.g., 2401.12345)")
    parser.add_argument("--metadata", help="Path to metadata JSON file")
    parser.add_argument("--analysis", help="Path to analysis JSON file")
    parser.add_argument("--reproduction", help="Path to reproduction JSON file")
    parser.add_argument("--citations", help="Path to citations JSON file")
    parser.add_argument("--language", choices=["english", "chinese"], default="english",
                        help="Report language (default: english)")
    parser.add_argument("--depth", choices=["shallow", "medium", "deep"], default="medium",
                        help="Analysis depth (default: medium)")
    parser.add_argument("--output", help="Output file path (default: ./alpha-sight/reports/{arxiv_id}_analysis.md)")
    parser.add_argument("--skill-path", help="Path to alpha-sight skill directory (optional)")

    args = parser.parse_args()

    # Initialize generator
    generator = ReportGenerator(skill_path=args.skill_path)

    # Set default output path
    if not args.output:
        # Get project root (4 levels up from scripts directory)
        script_dir = Path(__file__).parent
        project_root = script_dir.parent.parent.parent.parent
        args.output = project_root / "alpha-sight" / "reports" / f"{args.arxiv_id}_analysis.md"

    # Generate report
    print(f"Generating report for arXiv:{args.arxiv_id}...")
    print(f"Language: {args.language}")
    print(f"Depth: {args.depth}")

    try:
        report = generator.generate_from_files(
            arxiv_id=args.arxiv_id,
            metadata_file=args.metadata,
            analysis_file=args.analysis,
            reproduction_file=args.reproduction,
            citations_file=args.citations,
            language=args.language,
            depth=args.depth,
            output_file=args.output
        )

        print(f"\n✓ Report generated successfully")
        print(f"  Output: {args.output}")
        print(f"  Length: {len(report)} characters")

    except FileNotFoundError as e:
        print(f"✗ Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"✗ Error generating report: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
