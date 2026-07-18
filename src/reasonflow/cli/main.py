import typer

from reasonflow.workflows.analysis import RepositoryAnalysisWorkflow

app = typer.Typer(help="ReasonFlow - Production-grade AI workflow engine.")


@app.callback()
def main() -> None:
    """ReasonFlow CLI."""
    pass


@app.command()
def analyze(repository_url: str) -> None:
    typer.echo("🚀 ReasonFlow")

    workflow = RepositoryAnalysisWorkflow()
    workflow.run(repository_url)


if __name__ == "__main__":
    app()
