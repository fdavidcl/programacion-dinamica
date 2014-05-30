#!/bin/python
# encoding: utf8

from memoize import memoize
from math import sqrt

@memoize
def tsp(i, S):
    if len(S) == 0:
        return d[i][n-1]
    else:
        return min([d[i][j] + tsp(j,S - frozenset([j])) for j in S])


if __name__ == "__main__":
    # Lee ciudades
    n = int(input())
    points = []
    for i in range(n):
        x,y = raw_input().strip().split()
        x,y = int(x), int(y)
        points.append([x,y])

    # Matriz de distancias
    def dist(a,b):
        x,y = a
        z,w = b
        return sqrt((x-z)**2+(y-w)**2)

    d = [[dist(points[i],points[j]) for i in range(n)] for j in range(n)]
    
    # Resolución
    print "Distancia:",tsp(n-1,frozenset(range(n))-frozenset([n-1]))
