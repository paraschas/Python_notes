#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# William Dimitrios Paraschas (paraschas@gmail.com)


import signal
import sys
import time


def sigint_handler(signal, frame):
    """
    """
    print()
    print("Interrupted with CTRL-C, exiting...")

    sys.exit()


def perpetual():
    """
    """
    while True:
        print("Running, press CTRL-C to verify graceful termination.")
        time.sleep(1)


def handle_interupts_with_sigint_handler():
    """
    """
    # terminate gracefully on CTRL-C
    signal.signal(signal.SIGINT, sigint_handler)

    perpetual()


def handle_interupts_with_exception_handler():
    """
    """
    try:
        perpetual()
    except KeyboardInterrupt:
        print()
        print("Interrupted with CTRL-C, exiting...")
        sys.exit()


if __name__ == "__main__":
    # handle_interupts_with_sigint_handler()
    handle_interupts_with_exception_handler()
