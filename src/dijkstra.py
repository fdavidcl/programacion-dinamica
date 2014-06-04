#!/usr/bin/env python
# encoding: utf8

from math import sqrt
import Queue
import copy

def dijkstra_(s):
    padre = {}
    D = {}
    D[s] = 0
    
    for u in points - set([s]):
        D[u] = float("inf")
        padre[u] = None
    
    # Se ordena por distancia a s
    q = Queue.PriorityQueue()
    q.put((D[s],s))
    
    while not q.empty():
        u = q.get()
        for v in adyacencia[u]:
            if D[v] > D[u] + w[u][v]:
                D[v] = D[u] + w[u][v]
                padre[v] = u
                q.put((D[v],v))
    
    return padre
    
def dijkstra(s):
    D = {}
    D[s] = 0
    recorrer = copy.copy(points - set([s]))
    
    for u in points - set([s]):
        if dist[u,s] < float("inf"):
            D[u] = d[u,s]
        else:
            D[u] = float("inf")
    
    while recorrer:
        for v in recorrer:
            D[v] = min([D[k] + w[k,v] for k in points].append([D[v]])) 
        
        recorrer.remove(min(D))
    
    

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
    
