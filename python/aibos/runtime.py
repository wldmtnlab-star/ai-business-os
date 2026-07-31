"""
AIBOS Runtime
"""

from __future__ import annotations

from .loader import Loader
from .prompt_builder import PromptBuilder


class Runtime:
    """AIBOS Runtime."""

    def __init__(self, organization_dir: str):

        loader = Loader()

        self.resources = loader.load(organization_dir)

        self.builder = PromptBuilder()

    def build_prompt(
        self,
        playbook: str,
        inputs: dict,
    ) -> str:

        playbook_obj = self.resources["playbooks"][playbook]

        worker_name = playbook_obj.spec["workers"][0]

        worker = self.resources["workers"][worker_name]

        knowledge = [
            self.resources["knowledge"][name]
            for name in worker.spec.get("knowledge", [])
        ]

        return self.builder.build(
            worker=worker,
            knowledge=knowledge,
            playbook=playbook_obj,
            inputs=inputs,
        )