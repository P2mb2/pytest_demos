from unittest import mock

from myapp.numbers import guess_number
from myapp.requests import get_my_ip


# Mocking is the art of hardcode something that we can´t control on testing, so that we guarantee our test have always
# the same outcome.
# It is usually used on integration tests... we force the external system response so that we can test our code in a
# controlled way.

# Simple Mock Example:
# 1. We need to decorate our test and patch all calls that we want to mock. (the entire local scope)
# 2. For every patch that we made, a Mock Object will be passed as parameter to our test function.
# 3. We use return_value on the mock object to set the result that we want.

# This way... we replaced the call to get_number function and forced the return to 3... congratulations...
# you are a millionare now.

@mock.patch("myapp.numbers.get_number")
def test_guess_number(mock_get_number):
    mock_get_number.return_value = 3
    assert guess_number(3) == "You Won 1 Million Euros !!!!"


# Mock Example for requests.get
# This mock function will return a mock object. To use functions as result (json.return_value) we need to use dictionary
# unpacking

@mock.patch("myapp.requests.requests.get")
def test_get_my_ip(mock_get_request):
    mock_get_request.return_value = mock.Mock(name="mock response", **{"status_code": 200, "json.return_value": {
        "origin": "111.111.111.111"}})
    assert get_my_ip() == "111.111.111.111"

# There are another pretty usefull parameter in the mock object aside from return_value. That is side_effects
# side_effect allows you to define a function that is called whenever the Mock is called.
# This function is called with the same arguments as the mock.

# Side effect as Exception: the exception is raised every time the Mock is called.

# TODO: EXAMPLE

# Side effect as Iterable: each call to the mock will return the next value from the iterable.

# TODO: EXAMPLE
