#!/usr/bin/env python
# encoding: utf8

from graph import *

def bellman_ford(graph):
    # precondición: el grafo no debe contener ciclos de peso negativo
    n = graph['num_vertices']
    del graph['num_vertices']

    def algorithm(origen):
        distancia = [float('inf') for _ in xrange(n)]
        distancia[origen] = 0

        for _ in xrange(n-1):
            for (u,v) in graph:
                if distancia[u] + graph[(u,v)] < distancia[v]:
                    distancia[v] = distancia[u] + graph[(u,v)]

        return distancia

    return [algorithm(vertice) for vertice in xrange(n)]


if __name__ == "__main__":
    graph = readGraph()
    matrix = distanceMatrix(graph)

    print "Matriz de distancias:"
    printMatrix(matrix)

    print "Matriz de longitudes de caminos:"
    printMatrix(bellman_ford(graph))
