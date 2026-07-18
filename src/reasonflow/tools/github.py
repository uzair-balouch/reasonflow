from __future__ import annotations

from reasonflow.models.repository import Repository


class GitHubTool:
    """
    Operations related to GitHub repositories.
    """

    def fetch_metadata(self, repository: Repository) -> None:
        """
        Placeholder implementation.
        """
        print(f"Fetching metadata for {repository.url}")
