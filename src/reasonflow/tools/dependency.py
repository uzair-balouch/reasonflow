import base64
import tomllib

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

    def read_dependencies(
        self,
        repository: Repository,
        manifest: str,
    ) -> list[str]:

        response = httpx.get(
            f"{self.GITHUB_API}/repos/{repository.owner}/{repository.name}/contents/{manifest}"
        )

        response.raise_for_status()

        content = base64.b64decode(response.json()["content"]).decode()

        if manifest == "requirements.txt":
            return self._parse_requirements(content)

        if manifest == "pyproject.toml":
            return self._parse_pyproject(content)

        return []

    def _parse_requirements(
        self,
        content: str,
    ) -> list[str]:

        dependencies = []

        for line in content.splitlines():
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            package = line.split("==")[0].split(">=")[0].split("<=")[0].strip()

            dependencies.append(package)

        return dependencies

    def _parse_pyproject(
        self,
        content: str,
    ) -> list[str]:

        data = tomllib.loads(content)

        project = data.get("project", {})

        dependencies = []

        for dependency in project.get("dependencies", []):
            package = dependency.split(">=")[0].split("==")[0].split("<=")[0].strip()

            dependencies.append(package)

        return dependencies
