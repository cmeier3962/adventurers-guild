"""Tests for the sample application logic."""

import pytest

from your_project import greet
from your_project.__main__ import main


def test_greet_with_name() -> None:
    assert greet("Chris") == "Hello, Chris!"


def test_greet_uses_default_name() -> None:
    assert greet() == "Hello, World!"


def test_greet_strips_whitespace() -> None:
    assert greet("  Chris  ") == "Hello, Chris!"


def test_greet_rejects_empty_name() -> None:
    with pytest.raises(ValueError, match="Name cannot be empty"):
        greet("   ")


def test_main_prints_default_greeting(capsys: pytest.CaptureFixture[str]) -> None:
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"
