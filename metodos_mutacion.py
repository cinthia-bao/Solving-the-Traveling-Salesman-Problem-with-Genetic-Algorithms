import random


# La poblacion debe estar ordenada
def inseption(pob, porcentaje_base):
    porcentaje = int(porcentaje_base * len(pob) / 100)
    start_index = int((1 - porcentaje_base / 100) * len(pob))
    end_index = len(pob) - 1
    indices_seleccionados = set()
    a = len(pob[0]) - 3 
    corte1 = random.sample(range(1, a), 1)
    b = len(pob[0]) - 1 
    corte2 = random.sample(range(corte1[0] + 2, b), 1)
    for i in range(porcentaje):
        while True:
            indice = random.randint(start_index, end_index)
            if indice not in indices_seleccionados:
                indices_seleccionados.add(indice)
                break
        ind=pob[indice]
        p1 = ind[:corte1[0]]
        p2 = ind[corte1[0]:corte2[0]]
        p3 = ind[corte2[0]:len(ind)]
        p2 = p2[::-1]
        ind = p1 + p2 + p3
        pob[indice] = ind
    return pob

# La poblacion debe estar ordenada
def displacement(poblacion, porcentaje_base):
    porcentaje = int(porcentaje_base * len(poblacion)/100)
    start_index = int((1-porcentaje_base/100)*len(poblacion))
    end_index = len(poblacion)-1
    indices_seleccionados = set()
    a = len(poblacion[0]) - 3
    corte1 = random.sample(range(1, a), 1)
    b = len(poblacion[0]) - 1
    corte2 = random.sample(range(corte1[0] + 2, b), 1)
    for i in range(porcentaje):
        while True:
            indice = random.randint(start_index, end_index)
            if indice not in indices_seleccionados:
                indices_seleccionados.add(indice)
                break
        ind = poblacion[indice]
        p1 = ind[:corte1[0]]
        p2 = ind[corte1[0]:corte2[0]]
        p3 = ind[corte2[0]:len(ind)]
        posicion = random.randint(0, len(p1 + p3))   
        while posicion == corte1:
            posicion = random.randint(0, len(p1 + p3))
        nuevo_ind = (p1 + p3)[:posicion] + p2 + (p1 + p3)[posicion:]
        poblacion[indice]=  nuevo_ind
    return poblacion




