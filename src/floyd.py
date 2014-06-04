#!/usr/bin/env python
# encoding: utf8

from graph import *

if __name__ == "__main__":
    matrix = distanceMatrix(readGraph())
    printMatrix(matrix)
