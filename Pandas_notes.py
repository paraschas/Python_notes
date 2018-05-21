#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Dimitrios Paraschas (paraschas@gmail.com)


import pandas as pd


def check_if_dataframe_is_empty():
    """
    Check whether a dataframe is empty.
    """
    df = pd.DataFrame()

    if df.empty:
        print("The dataframe is empty:")
        print()
        print(df)


def main():
    """
    main function
    """
    check_if_dataframe_is_empty()


if __name__ == "__main__":
    main()
