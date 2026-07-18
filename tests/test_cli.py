from typer.testing import CliRunner

from reasonflow.cli.main import app

runner = CliRunner()


def test_analyze_command():
    result = runner.invoke(
        app,
        ["analyze", "https://github.com/psf/requests"],
    )

    assert result.exit_code == 0
    assert "Analyzing repository" in result.stdout
