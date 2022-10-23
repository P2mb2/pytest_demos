import sys

import pytest

from myapp.calculator import add, divide


# Mark Tests to group them together. Define groups on pytest.ini (Usually on test root)

# You can use groups to select tests to run
# pytest -v -m basic        :: Run only basic tests
# pytest -v -m "not basic"  :: Run all tests except basic
@pytest.mark.basic
def test_add_num():
    assert add(1, 2) == 3


@pytest.mark.basic
@pytest.mark.negative
def test_exception():
    with pytest.raises(ZeroDivisionError):
        assert divide(1, 0) == 1


# @pytest.mark.skip         :: Unconditional skip
# @pytest.mark.skipif       :: Skip test if condition met
# @pytest.mark.xfail        :: Expected to fail. Can be ignored when run with command pytest --runxfail
@pytest.mark.xfail(reason="Bug under analysis on ticket 123123")
def test_add_str():
    assert add("a", "b") == "ab"


@pytest.mark.skipif(sys.platform == "win32", reason="Dont run on Linux")
def test_add_str():
    assert add("a", "b") == "ab"
