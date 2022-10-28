class Developer:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


def get_older_developer(developers) -> Developer:
    return max(developers, key=lambda developer: developer.age)
