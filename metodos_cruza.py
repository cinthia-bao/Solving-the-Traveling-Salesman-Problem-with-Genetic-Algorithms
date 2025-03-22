

# Mapa de correspondencia parcial
def CPMX(padres1,padres2):
    errores =0
    hijo1 = []
    hijo2 = []
    for i in range(len(padres1)):
        p1 = padres1[i]
        p2 = padres2[i]
        corte =int( len(p1)/3)
        pmx1 = p1[corte:corte*2]
        pmx2 = p2[corte:corte*2]
        def sus(p1,pmx1,p2,pmx2):
            h1=[]
            for i in range(len(p1)):
                v1 = p1[i]
                if i < corte or corte*2-1 < i:
                    if v1 in pmx2:
                        indice = pmx2.index(v1)
                        nex = pmx1[indice]
                        while nex in pmx2:
                            indice = pmx2.index(nex)
                            nex= pmx1[indice]

                        v1 = pmx1[indice]
                        h1.append(v1)
                    else:
                        h1.append(v1)
                else:                                             
                    h1.append(p2[i])
            prueba=set(h1)
            z=len(prueba)/9
            if z!=1:
                print(f'Error en {i}')
                errores +=1
            return h1
        h1=sus(p1,pmx1,p2,pmx2)
        hijo1.append(h1)
        h2=sus(p2,pmx2,p1,pmx1)
        hijo2.append(h2)
    return hijo1, hijo2
    
# Cruza por ciclo
def cruza_ciclo(padre1, padre2):
    hijo1 = []
    hijo2 = []
    for i in range(len(padre1)):
        p1 = padre1[i]
        p2 = padre2[i]
        print('Padre 1', p1)
        print('Padre 2', p2)
        # Asegurarse de que los inicios sean diferentes
        if p1[0] == p2[0]:
            encontrado = False
            for j in range(i + 1, len(padre2)):
                if padre2[j][0] != p1[0]:
                    p2 = padre2[j]
                    encontrado = True
                    break
            if not encontrado:
                for j in range(i - 1, -1, -1):
                    if padre2[j][0] != p1[0]:
                        p2 = padre2[j]
                        break
        v1 = p1[0]
        i_local = 0
        vnew = None
        ciclo = [v1]
        while vnew != v1:
            vnew = p2[i_local]
            ciclo.append(vnew)
            i_local = p1.index(vnew)
            vnew = p2[i_local]
        def mantener_ciclos(p1, p2, ciclo):
            h1 = []
            for i in range(len(p1)):
                vi = p1[i]
                if vi in ciclo:
                    h1.append(vi)
                else:
                    h1.append(p2[i])
            return h1
        h1 = mantener_ciclos(p1, p2, ciclo)
        h2 = mantener_ciclos(p2, p1, ciclo)
        hijo1.append(h1)
        hijo2.append(h2)
    return hijo1, hijo2

    

