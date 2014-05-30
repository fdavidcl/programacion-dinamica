#!/bin/python
# encoding: utf8

from memoize import memoize

@memoize
def tsp(i, S):
    if len(S) == 0:
        return dist[i][n-1]
    else:
        return min([d[i][j] + tsp(j,S - frozenset([j]))] for j in S)
