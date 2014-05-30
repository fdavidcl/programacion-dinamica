#!/bin/python
# encoding: utf8

from memoize import memoize

coins = []

@memoize
def nCoins(price):
    if price == 0:
        return 0
    else:
        return min([1+ nCoins(price - m) for m in coins])
