"""Allow the package to run with `python -m your_project`."""

from your_project import greet


def main() -> None:
    """Run the sample application."""
    print(greet())


if __name__ == "__main__":
    main()
