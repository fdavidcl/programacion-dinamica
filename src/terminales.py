#!/bin/python
# encoding: utf8

from memoize import memoize

@memoize
def nCoins(price):
    if price == 0:
        return 0
    else:
        return min([1+nCoins(price-m) for m in coins if price-m >= 0])


if __name__ == "__main__":
    print "Introduzca monedas: "
    coins = map(int, raw_input().split())
    print "Introduzca precio:  "
    price = int(input())
    
    print "Son necesarias: ", nCoins(price), " monedas"
