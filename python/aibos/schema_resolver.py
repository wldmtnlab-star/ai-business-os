"""
AIBOS Schema Resolver

Maps AIBOS resource kinds to JSON Schema files.
"""

from pathlib import Path

from .exceptions import SchemaNotFoundError


class SchemaResolver:
    """Resolve schema files from AIBOS resource kinds."""

    def __init__(self, schema_dir: str | Path = "schemas") -> None:
        self.schema_dir = Path(schema_dir)

    def resolve(self, kind: str) -> Path:
        """
        Resolve a JSON Schema path.

        Example:
            Organization -> organization.schema.json
        """

        filename = f"{kind.lower()}.schema.json"
        schema_path = self.schema_dir / filename

        if not schema_path.exists():
            raise SchemaNotFoundError(
                f"Schema not found: {filename}"
            )

        return schema_path