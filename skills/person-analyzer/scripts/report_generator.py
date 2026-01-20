"""
Report generator for person-analyzer skill.
Generates comprehensive biographical analysis reports.
"""

import json
from typing import Dict, Any, Optional
from pathlib import Path
from datetime import datetime
from jinja2 import Template


class ReportGenerator:
    """Generate biographical analysis reports."""

    def __init__(self, language: str = "chinese", depth: str = "medium"):
        """
        Initialize report generator.

        Args:
            language: Report language (chinese or english)
            depth: Analysis depth (shallow, medium, deep)
        """
        self.language = language
        self.depth = depth

    def load_template(self, template_path: Path) -> Template:
        """
        Load report template.

        Args:
            template_path: Path to template file

        Returns:
            Jinja2 template
        """
        with open(template_path, "r", encoding="utf-8") as f:
            template_content = f.read()
        return Template(template_content)

    def prepare_template_data(
        self,
        person_name: str,
        domain: str,
        all_dimensions: Dict[str, Dict[str, Any]],
        credibility_data: Dict[str, Any],
        sources_data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Prepare data for template rendering.

        Args:
            person_name: Name of the person
            domain: Analysis domain
            all_dimensions: Data for all dimensions
            credibility_data: Credibility assessment data
            sources_data: Sources information

        Returns:
            Dictionary with template data
        """
        # Basic information
        template_data = {
            "person_name": person_name,
            "analysis_date": datetime.now().strftime("%Y-%m-%d"),
            "domain": domain,
            "depth": self.depth,
            "credibility_score": credibility_data.get("overall_credibility", 0),
            "is_entrepreneur": domain == "entrepreneur",
            "timeline_enabled": True,  # Can be made configurable
        }

        # Dimension 1: Family Background
        dim1 = all_dimensions.get("dimension1", )
        template_data.update(
            {
                "birth_date": dim1.get("birth_date", "Unknown"),
                "birth_place": dim1.get("birth_place", "Unknown"),
                "parents_background": dim1.get("parents_background", ""),
                "family_influence": dim1.get("family_influence", ""),
                "special_childhood_experiences": dim1.get(
                    "special_childhood_experiences", ""
                ),
                "operating_system_formation": dim1.get(
                    "operating_system_formation", ""
                ),
                "worldview": dim1.get("worldview", ""),
                "character": dim1.get("character", ""),
                "thinking_model": dim1.get("thinking_model", ""),
                "behavior_patterns": dim1.get("behavior_patterns", ""),
                "social_capital": dim1.get("social_capital", ""),
                "dimension1_sources": dim1.get("sources", []),
            }
        )

        # Dimension 2: Education
        dim2 = all_dimensions.get("dimension2", {})
        template_data.update(
            {
                "education_timeline": dim2.get("education_timeline", []),
                "academic_performance": dim2.get("academic_performance", ""),
                "student_leadership": dim2.get("student_leadership", ""),
                "business_attempts": dim2.get("business_attempts", ""),
                "influential_books": dim2.get("influential_books", ""),
                "school_adventures": dim2.get("school_adventures", ""),
                "education_impact": dim2.get("education_impact", ""),
                "dimension2_sources": dim2.get("sources", []),
            }
        )

        # Dimension 3: Work Experience
        dim3 = all_dimensions.get("dimension3", {})
        template_data.update(
            {
                "work_experiences": dim3.get("work_experiences", []),
                "dimension3_sources": dim3.get("sources", []),
            }
        )

        # Dimension 4: Career Milestones (domain-specific)
        dim4 = all_dimensions.get("dimension4", {})
        career_title = self._get_career_milestone_title(domain)
        template_data.update(
            {
                "career_milestone_title": career_title,
                "motivation": dim4.get("motivation", ""),
                "opportunity_discovery": dim4.get("opportunity_discovery", ""),
                "direction_determination": dim4.get("direction_determination", ""),
                "resource_integration": dim4.get("resource_integration", ""),
                "team_building": dim4.get("team_building", ""),
                "ventures": dim4.get("ventures", []),
                "career_anchor": dim4.get("career_anchor", ""),
                "professional_spirit": dim4.get("professional_spirit", ""),
                "dimension4_sources": dim4.get("sources", []),
            }
        )

        # Dimension 5: Learning Ability
        dim5 = all_dimensions.get("dimension5", {})
        template_data.update(
            {
                "learning_methods": dim5.get("learning_methods", ""),
                "learning_sources": dim5.get("learning_sources", ""),
                "mentorship": dim5.get("mentorship", ""),
                "core_friends": dim5.get("core_friends", []),
                "cognitive_leaps": dim5.get("cognitive_leaps", ""),
                "growth_journey": dim5.get("growth_journey", ""),
                "enlightenment_moments": dim5.get("enlightenment_moments", ""),
                "awakening_moments": dim5.get("awakening_moments", ""),
                "mentor_help": dim5.get("mentor_help", ""),
                "wisdom_upgrade": dim5.get("wisdom_upgrade", ""),
                "dimension5_sources": dim5.get("sources", []),
            }
        )

        # Dimension 6: Life Trajectory
        dim6 = all_dimensions.get("dimension6", {})
        template_data.update(
            {
                "social_class_trajectory": dim6.get("social_class_trajectory", []),
                "geographic_trajectory": dim6.get("geographic_trajectory", []),
                "critical_nodes": dim6.get("critical_nodes", []),
                "social_class_chart": dim6.get("social_class_chart", ""),
                "geographic_map": dim6.get("geographic_map", ""),
                "dimension6_sources": dim6.get("sources", []),
            }
        )

        # Dimension 7: Success Logic
        dim7 = all_dimensions.get("dimension7", {})
        template_data.update(
            {
                "success_logic": dim7.get("success_logic", []),
                "replicable_patterns": dim7.get("replicable_patterns", ""),
                "non_replicable_factors": dim7.get("non_replicable_factors", ""),
                "insights": dim7.get("insights", []),
                "dimension7_sources": dim7.get("sources", []),
            }
        )

        # Executive summary and highlights
        template_data.update(
            {
                "executive_summary": self._generate_executive_summary(
                    all_dimensions
                ),
                "highlights": self._extract_highlights(all_dimensions),
            }
        )

        # Credibility data
        template_data.update(
            {
                "overall_credibility": credibility_data.get("overall_credibility", 0),
                "dim1_credibility": credibility_data.get("dimension1", 0),
                "dim2_credibility": credibility_data.get("dimension2", 0),
                "dim3_credibility": credibility_data.get("dimension3", 0),
                "dim4_credibility": credibility_data.get("dimension4", 0),
                "dim5_credibility": credibility_data.get("dimension5", 0),
                "dim6_credibility": credibility_data.get("dimension6", 0),
                "dim7_credibility": credibility_data.get("dimension7", 0),
                "dim1_sources_count": len(dim1.get("sources", [])),
                "dim2_sources_count": len(dim2.get("sources", [])),
                "dim3_sources_count": len(dim3.get("sources", [])),
                "dim4_sources_count": len(dim4.get("sources", [])),
                "dim5_sources_count": len(dim5.get("sources", [])),
                "dim6_sources_count": len(dim6.get("sources", [])),
                "dim7_sources_count": len(dim7.get("sources", [])),
                "dim1_validation_status": credibility_data.get(
                    "dim1_validation_status", "Unknown"
                ),
                "dim2_validation_status": credibility_data.get(
                    "dim2_validation_status", "Unknown"
                ),
                "dim3_validation_status": credibility_data.get(
                    "dim3_validation_status", "Unknown"
                ),
                "dim4_validation_status": credibility_data.get(
                    "dim4_validation_status", "Unknown"
                ),
                "dim5_validation_status": credibility_data.get(
                    "dim5_validation_status", "Unknown"
                ),
                "dim6_validation_status": credibility_data.get(
                    "dim6_validation_status", "Unknown"
                ),
                "dim7_validation_status": credibility_data.get(
                    "dim7_validation_status", "Unknown"
                ),
                "conflicts": credibility_data.get("conflicts", []),
                "unverified_info": credibility_data.get("unverified_info", []),
            }
        )

        # Sources data
        template_data.update(
            {
                "google_ai_queries": sources_data.get("google_ai_queries", 0),
                "tavily_queries": sources_data.get("tavily_queries", 0),
                "firecrawl_pages": sources_data.get("firecrawl_pages", 0),
                "high_credibility_sources": sources_data.get(
                    "high_credibility_sources", []
                ),
                "medium_credibility_sources": sources_data.get(
                    "medium_credibility_sources", []
                ),
                "low_credibility_sources": sources_data.get(
                    "low_credibility_sources", []
                ),
            }
        )

        # Methodology
        template_data.update(
            {
                "data_collection_method": sources_data.get(
                    "data_collection_method", ""
                ),
                "validation_method": sources_data.get("validation_method", ""),
                "credibility_assessment_method": sources_data.get(
                    "credibility_assessment_method", ""
                ),
                "limitations": sources_data.get("limitations", ""),
            }
        )

        # Metadata
        template_data.update(
            {
                "generation_timestamp": datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                "analysis_duration": sources_data.get("analysis_duration", "Unknown"),
            }
        )

        return template_data

    def _get_career_milestone_title(self, domain: str) -> str:
        """Get career milestone title based on domain."""
        titles = {
            "entrepreneur": "创业经历"
            if self.language == "chinese"
            else "Entrepreneurial Journey",
            "scientist": "学术里程碑"
            if self.language == "chinese"
            else "Academic Milestones",
            "artist": "艺术生涯" if self.language == "chinese" else "Artistic Career",
            "politician": "政治生涯"
            if self.language == "chinese"
            else "Political Career",
            "athlete": "运动生涯" if self.language == "chinese" else "Athletic Career",
            "all": "职业里程碑" if self.language == "chinese" else "Career Milestones",
        }
        return titles.get(domain, titles["all"])

    def _generate_executive_summary(
        self, all_dimensions: Dict[str, Dict[str, Any]]
    ) -> str:
        """Generate executive summary from all dimensions."""
        # This is a placeholder - in real implementation, this would use
        # Claude to generate a comprehensive summary
        return "Executive summary to be generated based on all collected data."

    def _extract_highlights(
        self, all_dimensions: Dict[str, Dict[str, Any]]
    ) -> list:
        """Extract key highlights from all dimensions."""
        # This is a placeholder - in real implementation, this would extract
        # the most important achievements and moments
        return [
            "Highlight 1 to be extracted",
            "Highlight 2 to be extracted",
            "Highlight 3 to be extracted",
        ]

    def generate_report(
        self,
        template_path: Path,
        output_path: Path,
        person_name: str,
        domain: str,
        all_dimensions: Dict[str, Dict[str, Any]],
        credibility_data: Dict[str, Any],
        sources_data: Dict[str, Any],
    ) -> Path:
        """
        Generate complete report.

        Args:
            template_path: Path to template file
            output_path: Path to output file
            person_name: Name of the person
            domain: Analysis domain
            all_dimensions: Data for all dimensions
            credibility_data: Credibility assessment data
            sources_data: Sources information

        Returns:
            Path to generated report
        """
        # Load template
        template = self.load_template(template_path)

        # Prepare data
        template_data = self.prepare_template_data(
            person_name, domain, all_dimensions, credibility_data, sources_data
        )

        # Render template
        report_content = template.render(**template_data)

        # Save report
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report_content)

        return output_path


    def generate_report_sections(
        self,
        template_path: Path,
        person_name: str,
        domain: str,
        all_dimensions: Dict[str, Dict[str, Any]],
        credibility_data: Dict[str, Any],
        sources_data: Dict[str, Any],
    ) -> Dict[str, str]:
        """
        Generate report content split into sections for incremental writing.

        This method generates the report in 10 separate parts to avoid token limits
        when writing large reports. Each part corresponds to a major section.

        Args:
            template_path: Path to template file
            person_name: Name of the person
            domain: Analysis domain
            all_dimensions: Data for all dimensions
            credibility_data: Credibility assessment data
            sources_data: Sources information

        Returns:
            Dictionary with section names as keys and content as values
        """
        # Prepare template data
        template_data = self.prepare_template_data(
            person_name, domain, all_dimensions, credibility_data, sources_data
        )

        # Load template
        template = self.load_template(template_path)

        # Generate full content first
        full_content = template.render(**template_data)

        # Split into sections based on markdown headers
        sections = {}
        lines = full_content.split('\n')

        current_section = "part1_header_and_summary"
        current_content = []
        section_count = 1

        for line in lines:
            # Check if this is a major section header (## 一、二、三... or ## 十)
            if line.startswith('## 一、') or (current_section == "part1_header_and_summary" and line.startswith('---')):
                # Save previous section if it has content
                if current_content:
                    sections[current_section] = '\n'.join(current_content)
                    current_content = []

                # Start new section
                if line.startswith('## 一、'):
                    current_section = "part1_family_background"
                    section_count = 1

            elif line.startswith('## 二、'):
                sections[current_section] = '\n'.join(current_content)
                current_section = "part2_education"
                current_content = []
                section_count = 2

            elif line.startswith('## 三、'):
                sections[current_section] = '\n'.join(current_content)
                current_section = "part3_work_experience"
                current_content = []
                section_count = 3

            elif line.startswith('## 四、'):
                sections[current_section] = '\n'.join(current_content)
                current_section = "part4_career_milestones"
                current_content = []
                section_count = 4

            elif line.startswith('## 五、'):
                sections[current_section] = '\n'.join(current_content)
                current_section = "part5_learning_ability"
                current_content = []
                section_count = 5

            elif line.startswith('## 六、'):
                sections[current_section] = '\n'.join(current_content)
                current_section = "part6_life_trajectory"
                current_content = []
                section_count = 6

            elif line.startswith('## 七、'):
                sections[current_section] = '\n'.join(current_content)
                current_section = "part7_success_logic"
                current_content = []
                section_count = 7

            elif line.startswith('## 八、'):
                sections[current_section] = '\n'.join(current_content)
                current_section = "part8_failures"
                current_content = []
                section_count = 8

            elif line.startswith('## 九、'):
                sections[current_section] = '\n'.join(current_content)
                current_section = "part9_relationships"
                current_content = []
                section_count = 9

            elif line.startswith('## 十、'):
                sections[current_section] = '\n'.join(current_content)
                current_section = "part10_credibility_and_footer"
                current_content = []
                section_count = 10

            current_content.append(line)

        # Save the last section
        if current_content:
            sections[current_section] = '\n'.join(current_content)

        return sections


if __name__ == "__main__":
    # Test report generator
    print("Report generator initialized")
    generator = ReportGenerator(language="chinese", depth="medium")
    print(f"Language: {generator.language}")
    print(f"Depth: {generator.depth}")
