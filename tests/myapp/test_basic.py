from tests.context import calculator
import pytest


def test_add_num():
    assert calculator.add(1, 2) == 3


def test_add_str():
    assert calculator.add("a", "b") == "ab"


# Assert Exception Type
def test_exception():
    with pytest.raises(ZeroDivisionError):
        assert calculator.divide(1, 0) == 1


# Assert Exception Type and Text
def test_exception_text():
    with pytest.raises(ValueError, match="Input values must be integers"):
        assert calculator.add_only_ints("a", "b")


# Nested Tests on Class
class TestClassSample:
    def test_add_num_within_class(self):
        assert calculator.add(1, 2) == 3

    def test_add_str_within_class(self):
        assert calculator.add("a", "b") == "ab"
