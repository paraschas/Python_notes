#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# William Dimitrios Paraschas (paraschas@gmail.com)


def running_inside_docker():
    """
    Detect whether the program is running inside a Docker container instance.
    """
    path = "/proc/1/cgroup"

    with open(path) as f:
        contents = f.read()

    return "docker" in contents


def main():
    """
    main function
    """
    if running_inside_docker():
        print("running inside a Docker instance")
    else:
        print("no Docker instance detected")


if __name__ == "__main__":
    main()
