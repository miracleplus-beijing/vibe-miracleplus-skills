"""
Configuration loader for person-analyzer skill.
Handles environment variables, directory structure, and domain templates.
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, Optional
from dotenv import load_dotenv


class ConfigLoader:
    """Load and manage configuration for person-analyzer."""

    def __init__(self, skill_dir: Path):
        """
        Initialize configuration loader.

        Args:
            skill_dir: Path to the person-analyzer skill directory
        """
        self.skill_dir = Path(skill_dir)
        self.config_dir = self.skill_dir / "config"
        self.reports_dir = self.skill_dir / "reports"
        self.data_dir = self.skill_dir / "data"
        self.cache_dir = self.skill_dir / "cache"
        self.assets_dir = self.skill_dir / "assets"
        self.scripts_dir = self.skill_dir / "scripts"
        self.references_dir = self.skill_dir / "references"

        # Load environment variables
        self._load_env()

    def _load_env(self):
        """Load environment variables from multiple sources."""
        # Priority 1: Project-level .env
        project_env = self.skill_dir / ".env"
        if project_env.exists():
            load_dotenv(project_env)
            return

        # Priority 2: Global-level .env
        global_env = Path.home() / ".config" / "person-analyzer" / ".env"
        if global_env.exists():
            load_dotenv(global_env)
            return

        # Priority 3: System environment variables (already loaded)

    def ensure_directories(self):
        """Create directory structure if it doesn't exist."""
        directories = [
            self.config_dir,
            self.reports_dir / "entrepreneur",
            self.reports_dir / "scientist",
            self.reports_dir / "artist",
            self.reports_dir / "politician",
            self.reports_dir / "athlete",
            self.reports_dir / "general",
            self.data_dir,
            self.cache_dir,
            self.assets_dir,
            self.scripts_dir,
            self.references_dir,
        ]

        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)

    def get_api_keys(self) -> Dict[str, Optional[str]]:
        """
        Get API keys from environment variables.

        Returns:
            Dictionary with API keys (None if not set)
        """
        return {
            "tavily_api_key": os.getenv("TAVILY_API_KEY"),
            "firecrawl_api_key": os.getenv("FIRECRAWL_API_KEY"),
        }

    def load_domain_templates(self) -> Dict[str, Any]:
        """
        Load domain-specific question templates.

        Returns:
            Dictionary with domain templates
        """
        template_file = self.config_dir / "domain_templates.json"

        if not template_file.exists():
            # Create default templates
            default_templates = self._get_default_domain_templates()
            with open(template_file, "w", encoding="utf-8") as f:
                json.dump(default_templates, f, indent=2, ensure_ascii=False)
            return default_templates

        with open(template_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def _get_default_domain_templates(self) -> Dict[str, Any]:
        """Get default domain-specific question templates."""
        return {
            "entrepreneur": {
                "dimension4_title": "创业经历",
                "dimension4_title_en": "Entrepreneurial Journey",
                "specific_questions": [
                    "创业梦想如何点燃",
                    "商业机会发现",
                    "创业方向确定",
                    "资源整合",
                    "团队组建",
                    "融资历程",
                    "股权分配",
                    "高光时刻",
                    "至暗时刻",
                    "创业锚点",
                    "企业家精神",
                ],
            },
            "scientist": {
                "dimension4_title": "学术里程碑",
                "dimension4_title_en": "Academic Milestones",
                "specific_questions": [
                    "研究兴趣形成",
                    "重要研究突破",
                    "学术合作",
                    "获得的荣誉",
                    "研究方向转变",
                    "学术影响力",
                    "科研精神",
                ],
            },
            "artist": {
                "dimension4_title": "艺术生涯",
                "dimension4_title_en": "Artistic Career",
                "specific_questions": [
                    "艺术风格形成",
                    "代表作品",
                    "创作突破",
                    "艺术合作",
                    "获得的认可",
                    "风格演变",
                    "艺术精神",
                ],
            },
            "politician": {
                "dimension4_title": "政治生涯",
                "dimension4_title_en": "Political Career",
                "specific_questions": [
                    "从政动机",
                    "政治理念形成",
                    "重要政绩",
                    "政治联盟",
                    "危机处理",
                    "政治遗产",
                    "领导力体现",
                ],
            },
            "athlete": {
                "dimension4_title": "运动生涯",
                "dimension4_title_en": "Athletic Career",
                "specific_questions": [
                    "运动天赋发现",
                    "训练历程",
                    "重大比赛",
                    "突破性成就",
                    "伤病与恢复",
                    "职业转型",
                    "体育精神",
                ],
            },
            "all": {
                "dimension4_title": "职业里程碑",
                "dimension4_title_en": "Career Milestones",
                "specific_questions": [
                    "职业突破契机",
                    "关键机会识别",
                    "职业方向选择",
                    "资源获取",
                    "核心合作者",
                    "重要成就",
                    "职业转折",
                    "专业精神",
                ],
            },
        }

    def get_index_path(self) -> Path:
        """Get path to index.json file."""
        return self.skill_dir / "index.json"

    def load_index(self) -> Dict[str, Any]:
        """
        Load analysis index.

        Returns:
            Dictionary with analysis history
        """
        index_path = self.get_index_path()

        if not index_path.exists():
            default_index = {"analyses": [], "last_updated": None}
            with open(index_path, "w", encoding="utf-8") as f:
                json.dump(default_index, f, indent=2, ensure_ascii=False)
            return default_index

        with open(index_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_index(self, index_data: Dict[str, Any]):
        """
        Save analysis index.

        Args:
            index_data: Index data to save
        """
        index_path = self.get_index_path()
        with open(index_path, "w", encoding="utf-8") as f:
            json.dump(index_data, f, indent=2, ensure_ascii=False)

    def get_person_data_dir(self, person_name: str) -> Path:
        """
        Get data directory for a specific person.

        Args:
            person_name: Name of the person

        Returns:
            Path to person's data directory
        """
        # Normalize person name for directory
        normalized_name = person_name.replace(" ", "_").replace("/", "_")
        person_dir = self.data_dir / normalized_name
        person_dir.mkdir(parents=True, exist_ok=True)

        # Create subdirectories
        (person_dir / "dimensions").mkdir(exist_ok=True)

        return person_dir

    def get_report_path(self, person_name: str, domain: str, language: str) -> Path:
        """
        Get report path for a specific person.

        Args:
            person_name: Name of the person
            domain: Analysis domain
            language: Report language

        Returns:
            Path to report file
        """
        normalized_name = person_name.replace(" ", "_").replace("/", "_")
        domain_dir = self.reports_dir / domain
        domain_dir.mkdir(parents=True, exist_ok=True)

        suffix = "_zh" if language == "chinese" else "_en"
        return domain_dir / f"{normalized_name}_analysis{suffix}.md"


if __name__ == "__main__":
    # Test configuration loader
    import sys

    if len(sys.argv) > 1:
        skill_dir = Path(sys.argv[1])
    else:
        skill_dir = Path(__file__).parent.parent

    config = ConfigLoader(skill_dir)
    config.ensure_directories()

    print("✓ Directories created successfully")
    print(f"✓ Skill directory: {config.skill_dir}")
    print(f"✓ API keys loaded: {list(config.get_api_keys().keys())}")
    print(f"✓ Domain templates: {list(config.load_domain_templates().keys())}")
