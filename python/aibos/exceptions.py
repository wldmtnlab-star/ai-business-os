"""
AIBOS Exceptions

Custom exception hierarchy used throughout the AIBOS runtime.
"""


class AIBOSError(Exception):
    """Base exception for all AIBOS errors."""


class SchemaNotFoundError(AIBOSError):
    """Raised when a requested JSON Schema cannot be found."""


class ValidationError(AIBOSError):
    """Raised when schema validation fails."""