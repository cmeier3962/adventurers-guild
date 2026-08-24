from eryndor.enums import JobType


def test_job_type_values() -> None:
    """Tests that all job types exist with expected values."""
    assert JobType.DEFENDER.value == "Defender"
    assert JobType.ACOLYTE.value == "Acolyte"
    assert JobType.MARTIALIST.value == "Martialist"
    assert JobType.MARKSMAN.value == "Marksman"
    assert JobType.MYSTIC.value == "Mystic"


def test_job_type_count() -> None:
    """Tests that the expected number of foundation jobs exist."""
    assert len(JobType) == 5


def test_job_type_is_string_enum() -> None:
    """Tests that job types behave as strings."""
    assert isinstance(JobType.MARTIALIST, str)
    assert JobType.MARTIALIST == "Martialist"
