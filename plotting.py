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

    start = 0
    end = 10
    step = (end - start) / 100

    x = np.arange(start, end, step)
    y = slope * x

    fig, ax = plt.subplots()
    ax.plot(x, y)

    ax.set(
        xlabel="x", ylabel="y", title="linear function",
    )
    ax.grid()

    plt.show()


def graph(formula, start, end):
    step = (end - start) / 100
    x = np.arange(start, end, step)
    y = formula(x)
    plt.plot(x, y)
    plt.grid()
    plt.show()


def plot_any_function():
    def function_formula(x):
        return x ** 2 - 3 * x + 5

    start = -2
    end = 5

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
