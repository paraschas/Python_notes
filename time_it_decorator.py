#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# William Dimitrios Paraschas (paraschas@gmail.com)


import functools
import time


def time_it(verbose=True, show_arguments=False):
    """
    Decorator to measure function running time.
    """

    def time_it_decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            start_time = time.time()

            result = function(*args, **kwargs)

            end_time = time.time()
            total_time = end_time - start_time

            if verbose:
                function_name = function.__name__
                if show_arguments:
                    print(
                        f"{function_name}({args}, {kwargs}) run in {total_time:.6f} seconds"
                    )
                else:
                    print(f"{function_name} run in {total_time:.6f} seconds")
            return result

        return wrapper

    return time_it_decorator


@time_it()
def wait():
    print("wait started")
    delay = 1
    time.sleep(delay)
    print("wait finished")


def main():
    """
    main function
    """
    wait()


if __name__ == "__main__":
    main()
