#!/usr/bin/env python
# encoding: utf8

from graph import *


def dijkstra_algorithm(graph):
    n = graph['num_vertices']
    del graph['num_vertices']
    w = distanceMatrix(graph)
    
    def algorithm(s):
        padre = {}
        recorrer = range(n)
        recorrer.remove(s)

        d = [ w[s][v] for v in range(n) ]

        # Inicializamos los padres
        padre[s] = None
        for v in recorrer:
            if d[v] < float("inf"):
                padre[v] = s

        # Mientras queden nodos por recorrer
        while recorrer:
            u,v = min( [(d[i], i) for i in recorrer] )
            recorrer.remove(v)

            for a in recorrer:
                if d[v] + w[v][a] < d[a]:
                    d[a] = d[v] + w[v][a]
                    padre[a] = v

        return padre,d

    # Devuelve el camino desde el nodo 'origen' hasta i
    def decode_path(i,p):
        path = [i]

        while (p[i] is not None):
            path.append(p[i])
            i = p[i]

        return path[::-1]

    # Partiendo de todos los nodos aplicamos Dijkstra
    solucion = []
    
    for u in range(n):
        camino,distancia = algorithm(u)
        for v in range(n):
            if v is not u:
                path = [decode_path(v,camino)]
                path.append(distancia[v])
                solucion.append(path)

    return solucion


def print_paths(paths):
    for p in paths:
        print "Distancia: ", p.pop(), "\t\tCamino: ", p.pop()

if __name__ == "__main__":
    graph = readGraph()
    print_paths (dijkstra_algorithm(graph))
    
