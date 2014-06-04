#!/bin/python
# encoding: utf8

# Implementa funciones de lectura de grafos.
# Los grafos se representarán como conjunto de vértices y aristas o como
# matriz de distancias.

def readGraph ():
    """ 
    Formato:
        n
        e
        a b w
        a b w
        [...]
    
    Donde "n" es el número de vértices, "e" número de aristas. 
    Y cada arista es del tipo [a,b] con peso w: (a,b):w
    """
    
    # Define el grafo
    graph = {
        'num_vertices': 0
    }
    
    # Lee dimensión
    graph['num_vertices'] = int(input())
    e = int(input())
    
    # Lee aristas
    for i in range(e):
        a,b,w = raw_input().strip().split()
        a,b,w = int(a),int(b),int(w)
        graph[(a,b)] = w
        
        return graph


def distanceMatrix(graph):
    """ Da la matriz de distancias de un grafo. """
    def dist(a,b):
        if (a,b) in graph: 
            return graph[(a,b)]
        else:
            return float('inf')

    n = graph['num_vertices']
    return [[dist(a,b) for b in range(n)] for a in range(n)]
