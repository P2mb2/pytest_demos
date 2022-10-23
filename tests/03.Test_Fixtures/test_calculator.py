import json
import os

import pytest

from myapp.calculator import add_and_save_file, add_and_print_console
from myapp.developer import get_older_developer, Developer


# https://docs.pytest.org/en/7.1.x/reference/reference.html?highlight=fixtures%20list#fixtures
# Fixtures set a fixed baseline for tests. Fixtures are requested by test functions or other fixtures by declaring them
# as argument names.
# Default available fixtures:

#   1. tmpdir - delivers a temporary directory for filebase tests.

def test_add_and_save_file(tmpdir):
    filepath = os.path.join(tmpdir, "test.json")
    add_and_save_file(1, 2, filepath)
    assert json.load(open(filepath, 'r')) == {"a": 1, "b": 2, "result": 3}


#   2. capsys - text capturing of writes to sys.stdout and sys.stderr.

def test_add_and_print_console(capsys):
    add_and_print_console(1, 2)
    assert capsys.readouterr().out == "1 + 2 = 3\n"


# We can make our own fixtures. To share fixtures between packages, declare it on conftest.py.
#
# 1. Object Factory. Scope is very important.
#   function: the default scope, the fixture is destroyed at the end of the test.
#   class: the fixture is destroyed during teardown of the last test in the class.
#   module: the fixture is destroyed during teardown of the last test in the module.
#   package: the fixture is destroyed during teardown of the last test in the package.
#   session: the fixture is destroyed at the end of the test session.


def test_get_older_developer(developer_factory):
    developers = (
        developer_factory("Jota", 37),
        developer_factory("David", 27),
        developer_factory("Isabela", 25)
    )
    assert get_older_developer(developers).name == "Jota"


# We can also parametrize fixture with "params" and "request" objects.
@pytest.fixture(params=[("Jota", 50), ("Jota", 1)], ids=["old", "baby"])
def developer_parametrize_two_jotas(request) -> Developer:
    return Developer(request.param[0], request.param[1])


@pytest.mark.xfail(reason="will fail with baby age")
def test_get_older_developer_with_fixture_params(developer_parametrize_two_jotas):
    developers = (
        developer_parametrize_two_jotas,
        Developer("David", 26),
        Developer("Isabela", 27),
    )
    assert get_older_developer(developers).name == "Jota"


# Better... we can relate unit test parametrize object directly to fixture (using the name of the fixture as parameter
# itself)
# We need to use indirect and tell pytest witch parameters will be passed to the fixture (recieved on request).
@pytest.fixture
def developer_parametrize_two_jotas_noparams(request) -> Developer:
    return Developer(request.param[0], request.param[1])


@pytest.mark.parametrize(
    "developer_parametrize_two_jotas_noparams, result",
    [(("Jota", 50), "Jota"), (("Jota", 1), "Isabela")],
    indirect=["developer_parametrize_two_jotas_noparams"],
    ids=["Older_Jota", "Older_Isabela"])
def test_get_older_developer_connect_params_with_fixture(developer_parametrize_two_jotas_noparams, result: str):
    developers = (
        developer_parametrize_two_jotas_noparams,
        Developer("David", 26),
        Developer("Isabela", 27),
    )
    assert get_older_developer(developers).name == result
