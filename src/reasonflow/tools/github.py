from __future__ import annotations

from reasonflow.models.repository import Repository
from reasonflow.services.github import GitHubClient


class GitHubTool:
    """Tool to enrich a Repository object with data from GitHub to AI Agents."""

    def __init__(self, client: GitHubClient):
        self.client = client

    def enrich(self, repository: Repository) -> Repository:
        data = self.client.get_repository(
            repository.owner,
            repository.name,
        )

        repository.default_branch = data["default_branch"]
        repository.description = data["description"]
        repository.language = data["language"]
        repository.stars = data["stargazers_count"]

        license_info = data.get("license")

        if license_info:
            repository.license = license_info["spdx_id"]

        return repository
