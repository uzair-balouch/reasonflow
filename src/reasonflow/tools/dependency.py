import httpx

from reasonflow.models.repository import Repository


class DependencyTool:
    GITHUB_API = "https://api.github.com"

    SUPPORTED_MANIFESTS = {
        "requirements.txt",
        "pyproject.toml",
        "Pipfile",
        "poetry.lock",
        "package.json",
        "go.mod",
        "Cargo.toml",
    }

    def find_manifests(
        self,
        repository: Repository,
    ) -> list[str]:

        response = httpx.get(
            f"{self.GITHUB_API}/repos/{repository.owner}/{repository.name}/contents"
        )

        response.raise_for_status()

        manifests = []

        for item in response.json():
            if item["type"] != "file":
                continue

            if item["name"] in self.SUPPORTED_MANIFESTS:
                manifests.append(item["name"])

        return manifests
