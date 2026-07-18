from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Repository:
    """
    Represents a source code repository.
    """

    url: str
    owner: str
    name: str
    default_branch: str = "main"
    local_path: str | None = None
