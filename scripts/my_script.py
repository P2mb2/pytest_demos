from scripts.context import MyClient


def get_my_name() -> str:
    return "Jota"


if __name__ == "__main__":
    name = get_my_name()
    print(MyClient.get_greeting(name))
