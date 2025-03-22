from collections import Counter
import random

def elitismo(poblacion, aptitudes, n):
    if len(poblacion) < n:
        extra = n - len(poblacion)
        mejores = poblacion[:]
        ap_mejores = aptitudes[:]
        for _ in range(extra):
            idx = random.randint(0, len(mejores) - 1)
            mejores.append(mejores[idx])
            ap_mejores.append(ap_mejores[idx])
    else:
        mejores = poblacion[:n]
        ap_mejores = aptitudes[:n]

    return mejores, ap_mejores

