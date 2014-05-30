#!/bin/python

# Dada una función, devuelve una versión usando memoización.
# La función implementa una caché para conocer sus resultados ya calculados.
# Derivado de: http://technotroph.wordpress.com/2012/04/05/memoize-it-the-python-way/

def memoize(f):
    cache = {}
    
    def memoizedFunction(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    return memoizedFunction
