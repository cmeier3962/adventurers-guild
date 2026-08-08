"""Allow the package to run with `python -m eryndor`."""

from eryndor import greet


def main() -> None:
    """Run the sample application."""
    print(greet())


if __name__ == "__main__":
    main()
