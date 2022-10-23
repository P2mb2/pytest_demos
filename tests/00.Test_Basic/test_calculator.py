import pytest

from myapp.calculator import add, divide, add_only_ints


def test_add_num():
    assert add(1, 2) == 3


def test_add_str():
    assert add("a", "b") == "ab"


# Assert Exception Type
def test_exception():
    with pytest.raises(ZeroDivisionError):
        assert divide(1, 0) == 1


# Assert Exception Type and Text
def test_exception_text():
    with pytest.raises(ValueError, match="Input values must be integers"):
        assert add_only_ints("a", "b")


# Nested Tests on Class
class TestClassSample:
    def test_add_num_within_class(self):
        assert add(1, 2) == 3

    def test_add_str_within_class(self):
        assert add("a", "b") == "ab"
