
# METODO POR TOURNAMENT
def tournament(poblacion, parejas):
    padre1 = poblacion[:parejas]
    #ap_padre1 = ap_poblacion[:parejas]
    padre2 = poblacion[-1:-parejas-1:-1]
    #ap_padre2 = ap_poblacion[-1:-parejas-1:-1]
    return list(padre1), list(padre2)#, list(ap_padre1), list(ap_padre2)

def rank(poblacion ):
    padre1=[]
    padre2=[]
    for i in range(0,len(poblacion),2):
        p1=poblacion[i]
        p2=poblacion[i+1]
        padre1.append(p1)
        padre2.append(p2)
    return padre1,padre2 







