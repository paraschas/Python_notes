#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Dimitrios Paraschas (paraschas@gmail.com)


import pandas as pd


def test_if_dataframe_is_empty():
    empty_dataframe = pd.DataFrame()

    if empty_dataframe.empty:
        print("The dataframe is empty.")


def main():
    """
    main function
    """
    test_if_dataframe_is_empty()


if __name__ == "__main__":
    main()
