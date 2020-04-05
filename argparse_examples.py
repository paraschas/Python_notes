#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# William Dimitrios Paraschas (paraschas@gmail.com)


"""
argparse usage examples

https://docs.python.org/3/library/argparse.html
"""


import argparse
import sys


def echo(message):
    print(message)


def main():
    """
    main function
    """
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        "--exit", action="store_true", help="immediately stop execution"
    )
    argument_parser.add_argument("message", nargs="+", help="message to echo")

    args = argument_parser.parse_args()

    if not args.exit:
        message = " ".join(word for word in args.message)
        echo(message)


if __name__ == "__main__":
    main()
