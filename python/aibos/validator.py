"""
AIBOS Schema Validator

Validate AIBOS resources against JSON Schema.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

from .exceptions import ValidationError
from .schema_resolver import SchemaResolver


class Validator:
    """Validate AIBOS YAML resources."""

    def __init__(self, schema_dir: str | Path = "schemas") -> None:
        self.resolver = SchemaResolver(schema_dir)

    def load_yaml(self, file_path: str | Path) -> dict[str, Any]:
        """Load a YAML file."""

        file_path = Path(file_path)

        with file_path.open("r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def load_schema(self, schema_path: Path) -> dict[str, Any]:
        """Load a JSON Schema."""

        with schema_path.open("r", encoding="utf-8") as f:
            return json.load(f)

    def validate(self, yaml_file: str | Path) -> bool:
        """
        Validate an AIBOS resource.

        The JSON Schema is resolved automatically from the resource kind.
        """

        document = self.load_yaml(yaml_file)

        kind = document.get("kind")

        if not kind:
            raise ValidationError("Missing 'kind' field.")

        schema_path = self.resolver.resolve(kind)

        schema = self.load_schema(schema_path)

        validator = Draft202012Validator(schema)

        errors = sorted(
            validator.iter_errors(document),
            key=lambda e: list(e.absolute_path),
        )

        if errors:
            messages = []

            for error in errors:

                path = "/".join(map(str, error.absolute_path))

                if path:
                    messages.append(f"{path}: {error.message}")
                else:
                    messages.append(error.message)

            raise ValidationError(
                "\n".join(messages)
            )

        return True