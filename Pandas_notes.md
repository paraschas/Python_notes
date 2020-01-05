#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# William Dimitrios Paraschas (paraschas@gmail.com)


import pandas as pd


def check_if_dataframe_is_empty():
    """
    Check whether a dataframe is empty.

    http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.empty.html
    """
    df = pd.DataFrame()

    if df.empty:
        print("The dataframe is empty:")
        print()
        print(df)


def read_html():
    """
    Generate a list of dataframes from tables in an HTML page.

    https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_html.html
    """
    link = "https://docs.python.org/3/library/functions.html"
    match = "Built-in Functions"
    df_list = pd.read_html(io=link, match=match)

    print(df_list[0])


def main():
    """
    main function
    """
    # check_if_dataframe_is_empty()

    read_html()


if __name__ == "__main__":
    main()
