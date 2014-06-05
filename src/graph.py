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

    El grafo tendrá nodos [0..n-1], podrá accederse al peso de
    una arista concreta por: graph[(a,b)]
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
        a,b,w = int(a),int(b),float(w)
        graph[(a,b)] = w

    return graph



def distanceMatrix(graph):
    """ Da la matriz de distancias de un grafo. """
    def dist(a,b):
        # Caso de arista contenida en el grafo
        if (a,b) in graph:
            return graph[(a,b)]
        # Caso simétrico
        elif (b,a) in graph:
            return graph[(b,a)]
        # Caso reflexivo
        elif a == b:
            return 0
        # Caso de ausencia de arista
        else:
            return float('inf')

    n = graph['num_vertices']
    return [[dist(a,b) for b in range(n)] for a in range(n)]



def printMatrix(matrix):
    """ Imprime una matriz """
    for i in range(len(matrix)):
        print '(',
        for j in range(len(matrix[i])):
            print repr(matrix[i][j]).center(3),
        print ')'
