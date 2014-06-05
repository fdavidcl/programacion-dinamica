#!/usr/bin/env python
# encoding: utf8

from graph import *

def bellman_algorithm(origen, graph, n):
    distancia = [float('inf') for _ in xrange(n)]
    distancia[origen] = 0
    
    for _ in xrange(n-1):
        for (u,v) in graph:
            if distancia[u] + graph[(u,v)] < distancia[v]:
                distancia[v] = distancia[u] + graph[(u,v)]
     
    # Detección de ciclos de peso negativo
    for (u,v) in graph:
        if distancia[u] + graph[(u,v)] < distancia[v]:
            raise Exception("El grafo contiene un ciclo de peso negativo")


    return distancia


def bellman_ford(graph):
    n = graph['num_vertices']
    del graph['num_vertices']

    return [bellman_algorithm(vertice,graph,n) for vertice in xrange(n)]


if __name__ == "__main__":
    graph = readGraph()
    matrix = distanceMatrix(graph)

    print "Matriz de distancias:"
    printMatrix(matrix)

    print "Matriz de longitudes de caminos:"
    printMatrix(bellman_ford(graph))
