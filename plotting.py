#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# William Dimitrios Paraschas (paraschas@gmail.com)


import datetime as dt

import matplotlib.pyplot as plt
import numpy as np


def plot_ticker():
    import yfinance as yf

    tsla = yf.Ticker("TSLA")

    # print(tsla.info)
    symbol = "TSLA"
    start = dt.datetime(2012, 1, 1)
    end = dt.datetime(2020, 12, 31)

    data = yf.download(symbol, start=start, end=end)
    # print(data.head())

    data["High"].plot()
    plt.legend()
    plt.show()


def plot_linear_function():
    slope = 0.5

    x = np.arange(0, 10, 1)
    y = slope * x

    fig, ax = plt.subplots()
    ax.plot(x, y)

    ax.set(
        xlabel="x", ylabel="y", title="linear function",
    )
    ax.grid()

    plt.show()


def graph(formula, start, end):
    x_values = np.arange(start, end, (end - start) / 100)
    x = np.array(x_values)
    y = formula(x)
    plt.plot(x, y)
    plt.show()


def plot_any_function():
    def function_formula(x):
        return -x + 0.5

    start = -4
    end = 4

    graph(function_formula, start, end)


def main():
    """
    main function
    """
    # plot_ticker()

    # plot_linear_function()

    plot_any_function()


if __name__ == "__main__":
    main()
