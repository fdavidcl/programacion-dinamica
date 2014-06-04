#!/usr/bin/env python
# encoding: utf8

from graph import *

def floyd(graph):
    n = graph['num_vertices']
    dist = distanceMatrix(graph)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
                
    return dist


if __name__ == "__main__":
    graph = readGraph()
    matrix = distanceMatrix(graph)
    
    print "Matriz de distancias:"
    printMatrix(matrix)
    print "Matriz de longitudes de caminos:"
    printMatrix(floyd(graph))
