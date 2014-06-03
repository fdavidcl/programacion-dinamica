def num_coins(tipos, precio)
    monedas = []
    monedas[0] = 0

    for c in [0..precio]
        for m in tipos
            if (c+m <= precio &&
                (!monedas[c+m] || monedas[c] + 1 < monedas[c+m])
                monedas[c+m] = monedas[c] + 1

    return monedas[precio]
end
