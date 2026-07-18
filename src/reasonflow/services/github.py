from __future__ import annotations

import httpx


class GitHubClient:
    """A client for interacting with the GitHub API."""

    BASE_URL = "https://api.github.com"

    def __init__(self) -> None:
        self._client = httpx.Client(timeout=30)

    def get_repository(self, owner: str, repo: str) -> dict:
        response = self._client.get(f"{self.BASE_URL}/repos/{owner}/{repo}")

        response.raise_for_status()

        return response.json()

    def close(self) -> None:
        self._client.close()
