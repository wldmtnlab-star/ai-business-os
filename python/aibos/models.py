"""
AIBOS Data Models
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Organization:
    api_version: str
    kind: str
    metadata: dict[str, Any]
    spec: dict[str, Any]
    runtime: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class Knowledge:
    api_version: str
    kind: str
    metadata: dict[str, Any]
    content: str


@dataclass(slots=True)
class Worker:
    api_version: str
    kind: str
    metadata: dict[str, Any]
    spec: dict[str, Any]


@dataclass(slots=True)
class Playbook:
    api_version: str
    kind: str
    metadata: dict[str, Any]
    spec: dict[str, Any]