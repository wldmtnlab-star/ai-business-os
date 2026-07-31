"""
AIBOS Prompt Builder
"""

from __future__ import annotations

from .models import (
    Knowledge,
    Playbook,
    Worker,
)


class PromptBuilder:
    """Build prompts from AIBOS resources."""

    def build(
        self,
        worker: Worker,
        knowledge: list[Knowledge],
        playbook: Playbook,
        inputs: dict,
    ) -> str:
        """
        Build a system prompt.
        """

        sections: list[str] = []

        # Worker
        sections.append("# ROLE")
        sections.append(worker.spec["role"])
        sections.append("")

        sections.append("# GOAL")
        sections.append(worker.spec["goal"])
        sections.append("")

        # Constraints
        constraints = worker.spec.get("constraints", [])

        if constraints:
            sections.append("# CONSTRAINTS")

            for item in constraints:
                sections.append(f"- {item}")

            sections.append("")

        # Knowledge
        if knowledge:
            sections.append("# KNOWLEDGE")

            for doc in knowledge:
                sections.append(doc.content)
                sections.append("")

        # Playbook
        sections.append("# TASK")
        sections.append(playbook.spec["objective"])
        sections.append("")

        # Inputs
        if inputs:
            sections.append("# INPUT")

            for key, value in inputs.items():
                sections.append(f"{key}: {value}")

            sections.append("")

        return "\n".join(sections).strip()