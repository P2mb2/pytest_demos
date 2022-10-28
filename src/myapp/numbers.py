import random


def get_number() -> int:
    return random.randint(1, 1000000)


def guess_number(number: int) -> str:
    if get_number() != number:
        return "You Lost"
    return "You Won 1 Million Euros !!!!"
