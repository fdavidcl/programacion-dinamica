#!/usr/bin/env python
# encoding: utf8

from graph import readGraph
from dijkstra import dijkstra_algorithm, print_paths
from bellman import bellman_algorithm

def johnson(graph):
    n = graph['num_vertices']
    del graph['num_vertices']
    grafo = graph.copy()
    
    graph[(n,n)] = 0
    for i in range(n):
        graph[(i,n)] = graph[(n,i)] = 0
    
    # Aplicamos Bellman al grafo
    g = bellman_algorithm(n,graph,n+1)
    
    for (u,v) in grafo:
        grafo[(u,v)] += g[u] - g[v]

    # Aplicamos Dijkstra al grafo de nuevos pesos
    grafo['num_vertices'] = n
    paths = dijkstra_algorithm(grafo)
    
    # Sumamos g[v] - g[u] para volver a tener la distancia inicial
    for i in range(len(paths)):
        paths[i][-1] += g[paths[i][0][-1]] - g[paths[i][0][0]]
    
    return paths

if __name__ == "__main__":
    graph = readGraph()
    print_paths(johnson (graph))
    