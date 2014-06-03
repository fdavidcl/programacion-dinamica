def resuelve(precios)
    minimo = 0
    compra = 0
    venta = 0

    for i in [1..AAprecios]
        if (precios[i] < minimo)
            minimo = i

        beneficio = precios[i] - precios[minimo]

        if (beneficio > precios[venta] - precios[compra])
            compra = minimo
            venta = i

    return (compra, venta)
end
