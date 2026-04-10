import os
from pathlib import Path
from openapi_cli_gen import build_cli

# Base URL: override via OPENAI_REST_CLI_BASE_URL env var, fall back to spec default
_base_url = os.environ.get("OPENAI_REST_CLI_BASE_URL")

app = build_cli(
    spec=Path(__file__).parent / "spec.yaml",
    name="openai-rest-cli",
    base_url=_base_url,
)


def main():
    app()


if __name__ == "__main__":
    main()
