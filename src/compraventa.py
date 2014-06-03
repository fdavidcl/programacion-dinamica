#!/usr/bin/env python
# encoding: utf8

def compraventa():
    minimo = 0
    compra = 0
    venta = 0

    for i,p in zip(range(len(precios)),precios):
        if p < precios[minimo]:
            minimo = i

        if p - precios[minimo] > precios[venta] - precios[compra]:
            compra = minimo
            venta = i

    return compra,venta


if __name__ == "__main__":
    print "Introduce precios de acciones por días: "
    precios = map(float, raw_input().split())

    solucion = compraventa()

    if solucion[-1] is not solucion[0]:
        print "Día de compra/ Día de venta: ", solucion
        print "Beneficio: ", precios[solucion[-1]] - precios[solucion[0]]
    else:
        print "No se puede obtener beneficio en la compraventa"
