from random import choice
from string import (
    ascii_lowercase,
    ascii_uppercase,
    digits
)


def get_random_id():
    return "".join(
        choice(
            ascii_lowercase + ascii_uppercase + digits
        ) for _ in range(8))


if __name__ == "__main__":
    pass