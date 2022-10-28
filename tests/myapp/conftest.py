import pytest

from src.myapp.developer import Developer


@pytest.fixture
def developer_factory():
    def _make_new_developer(name, age) -> Developer:
        return Developer(name, age)

    return _make_new_developer
