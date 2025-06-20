def encontrar_distancias(cidade, distMax):

    v = []

    cidades = ['pg','curitiba','sjp', 'castro', 'paranagua']

    distancias = [[0,120, 140, 25,210],
    [120,0, 20, 145, 80],
    [140,20, 0, 140, 60],
    [20,140, 160, 0, 220],
    [210,80, 60, 220,0]]

    indCidade = cidades.index(cidade)
    distCidade = distancias[indCidade]

    for i in distCidade:
        if i <= distMax:
            indDistCidade = distCidade.index(i)
            cidEncontrada = cidades[indDistCidade]
            v.append(cidEncontrada)

    return v

print(encontrar_distancias("paranagua", 90))