"""
AIBOS Resource Loader
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from .models import (
    Knowledge,
    Organization,
    Playbook,
    Worker,
)


class Loader:
    """Load AIBOS resources."""

    def load_yaml(self, path: str | Path) -> dict[str, Any]:
        path = Path(path)

        with path.open("r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def load_markdown(self, path: str | Path) -> tuple[dict[str, Any], str]:
        path = Path(path)

        text = path.read_text(encoding="utf-8")

        if not text.startswith("---"):
            return {}, text

        _, frontmatter, content = text.split("---", 2)

        metadata = yaml.safe_load(frontmatter)

        return metadata, content.strip()

    def load_organization(self, organization_dir: Path) -> Organization:

        data = self.load_yaml(
            organization_dir / "organization.yaml"
        )

        return Organization(
            api_version=data["apiVersion"],
            kind=data["kind"],
            metadata=data["metadata"],
            spec=data["spec"],
            runtime=data.get("runtime", {}),
        )

    def load_knowledge(
        self,
        organization_dir: Path,
        organization: Organization,
    ) -> dict[str, Knowledge]:

        result = {}

        for name in organization.spec.get("knowledge", []):

            metadata, content = self.load_markdown(
                organization_dir / "knowledge" / f"{name}.md"
            )

            result[name] = Knowledge(
                api_version=metadata["apiVersion"],
                kind=metadata["kind"],
                metadata=metadata["metadata"],
                content=content,
            )

        return result

    def load_workers(
        self,
        organization_dir: Path,
        organization: Organization,
    ) -> dict[str, Worker]:

        result = {}

        for name in organization.spec.get("workers", []):

            data = self.load_yaml(
                organization_dir / "workers" / f"{name}.yaml"
            )

            result[name] = Worker(
                api_version=data["apiVersion"],
                kind=data["kind"],
                metadata=data["metadata"],
                spec=data["spec"],
            )

        return result

    def load_playbooks(
        self,
        organization_dir: Path,
        organization: Organization,
    ) -> dict[str, Playbook]:

        result = {}

        for name in organization.spec.get("playbooks", []):

            data = self.load_yaml(
                organization_dir / "playbooks" / f"{name}.yaml"
            )

            result[name] = Playbook(
                api_version=data["apiVersion"],
                kind=data["kind"],
                metadata=data["metadata"],
                spec=data["spec"],
            )

        return result

    def load(self, organization_dir: str | Path) -> dict[str, Any]:

        organization_dir = Path(organization_dir)

        organization = self.load_organization(
            organization_dir
        )

        knowledge = self.load_knowledge(
            organization_dir,
            organization,
        )

        workers = self.load_workers(
            organization_dir,
            organization,
        )

        playbooks = self.load_playbooks(
            organization_dir,
            organization,
        )

        return {
            "organization": organization,
            "knowledge": knowledge,
            "workers": workers,
            "playbooks": playbooks,
        }