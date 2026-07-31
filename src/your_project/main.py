"""Core application logic."""


def greet(name: str = "World") -> str:
    """Return a friendly greeting."""
    cleaned_name = name.strip()

    if not cleaned_name:
        raise ValueError("Name cannot be empty")

    return f"Hello, {cleaned_name}!"
