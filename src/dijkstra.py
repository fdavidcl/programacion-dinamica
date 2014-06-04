#!/usr/bin/env python
# encoding: utf8

from math import sqrt
    
def dijkstra(s):
    padre = {}
    padre[s] = None
    recorrer = range(n)
    recorrer.remove(s)
    
    D = [ d[s][i] for i in range(n) ]
    # Inicializamos los padres
    for i in recorrer:
        if D[i] < float("inf"):
            padre[i] = s
    
    while recorrer:
        w,v = min( [(D[k], k) for k in recorrer] ) 
        
        for i in range(len(recorrer)):
            a = recorrer[i]
            D[a],b = min( [(D[k] + d[k][a], k) for k in range(n)] )
            if a is not b:
                padre[a] = b
                
        recorrer.remove(v)
    
    return padre,D


def decodePath(i,p):
    path=str(i)

    while (p[i] is not None):
        path += " >- " + str(p[i])
        i = p[i]
        
    return path[::-1]
        
    
if __name__ == "__main__":
    n=5
    
    d=[[0,1,3,float("inf"),2],
       [9,0,float("inf"),float("inf"),7],
       [9,5,0,float("inf"),7],
       [9,4,2.5,0,float("inf")],
       [float("inf"),4,2.5,5,0]]
    
    for i in range(n-1):
        p,D = dijkstra(i)
        for j in range(n-1):
            print "Camino: ", decodePath(j,p), "\t\tDistancia: ", D[j]
