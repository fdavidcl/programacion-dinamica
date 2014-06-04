#!/usr/bin/env python
# encoding: utf8

from graph import readGraph


def dijkstra_algorithm(graph):
    n = graph['num_vertices']
    del graph['num_vertices']
    w = [[graph[(u,v)] for v in range(n)] for u in range(n)]
    
    def algorithm(s):
        padre = {}
        recorrer = range(n)
        recorrer.remove(s)
        
        d = [ w[s][i] for i in range(n) ]
        
        # Inicializamos los padres
        padre[s] = None
        for i in recorrer:
            if d[i] < float("inf"):
                padre[i] = s
        
        # Mientras queden nodos por recorrer
        while recorrer:
            u,v = min( [(d[k], k) for k in recorrer] ) 
            
            for i in range(len(recorrer)):
                a = recorrer[i]
                d[a],b = min( [(d[k] + w[k][a], k) for k in range(n)] )
                if a is not b:
                    padre[a] = b
                    
            recorrer.remove(v)
        
        return padre,d

    # Devuelve el camino hasta el nodo origen partiendo de i
    def decode_path(i,p):
        path=str(i)

        while (p[i] is not None):
            path += " >- " + str(p[i])
            i = p[i]
            
        return path[::-1]
        
    # Partiendo de todos los nodos aplicamos Dijkstra
    for u in range(n):
        camino,distancia = algorithm(u)
        for v in range(n):
            if v is not u:
                print "Camino: ", decode_path(v,camino), "\t\tDistancia: ", distancia[v]

if __name__ == "__main__":
    graph = readGraph()
    dijkstra_algorithm(graph)
