from what_is_year_now import what_is_year_now
import pytest
from unittest.mock import MagicMock, patch


def test_current_year_ymd_format():
    actual = what_is_year_now()
    expected = 2020
    assert actual == expected


def test_current_year_dmy_format():
    actual = what_is_year_now()

    expected = 2020
    assert actual == expected

