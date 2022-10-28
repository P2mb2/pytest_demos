import pytest

from src.myapp import calculator


# Perform multiple calls with different parameters.
# 1. Define parameter variable names and use them on the test function
# 2. Define a tuple of possible combinations for defined parameters
# 3. Give meaningful names to each test run.

@pytest.mark.parametrize("a,b,result",
                         [(1, 2, 3), ("a", "b", "ab"), ([1, 2], [3], [1, 2, 3])],
                         ids=["int", "str", "list"])
def test_add_num(a, b, result):
    assert calculator.add(a, b) == result
