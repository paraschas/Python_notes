#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# William Dimitrios Paraschas (paraschas@gmail.com)


import secrets
import string


def generate_password(length=64):
    """
    Generate an alphanumeric password, starting and ending with an ASCII letter,
    and at least two of lowercase characters, uppercase characters, and digits.
    """
    alphabet = string.ascii_letters + string.digits

    while True:
        password = "".join([secrets.choice(alphabet) for _ in range(length)])
        if (
            all(password[index] in string.ascii_letters for index in [0, -1])
            and sum(char.islower() for char in password) >= 2
            and sum(char.isupper() for char in password) >= 2
            and sum(char.isdigit() for char in password) >= 2
        ):
            break

    return password


def main():
    """
    main function
    """
    password = generate_password()
    print(password)


if __name__ == "__main__":
    main()
