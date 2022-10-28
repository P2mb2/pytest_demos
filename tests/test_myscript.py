from tests.context import get_my_name


def test_greetings():
    assert get_my_name() == "Jota"
