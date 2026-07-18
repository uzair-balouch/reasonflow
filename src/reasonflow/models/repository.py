from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class Repository:
    url: str
    owner: str
    name: str

    default_branch: str | None = None
    description: str | None = None
    language: str | None = None
    license: str | None = None
    stars: int = 0
    local_path: Path | None = None
