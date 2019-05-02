import numpy
import os
import math

# nvariables = input("Ingrese el numero de variables -> ")

def comprobar(resultados, nvariables, condicion):

    if condicion and condicion[-1] <= 0:
        return True
    c = 0
    limit = len(resultados)
    for i in range(nvariables):
        if resultados[limit-1][i] == resultados[limit-2][i]: c += 1
    if c == nvariables: return True
    else: return False

if __name__ == "__main__":
    os.system("clear")

    file = open("datos.txt")
    data = file.read().strip()
    file.close()

    ecuaciones = [[float(num) for num in line.strip().split()] for line in data.split('\n')]
    print(ecuaciones)

    nvariables = len(ecuaciones)

    resultados = []
    resultado = []
    for i in range(nvariables):
        resultado.append(ecuaciones[i][nvariables])
    resultados.append(resultado)

    niteracion = 0
    condicion = []
    while True:
        resultado = []
        for f in range(nvariables):
            result = 0
            for c in range(nvariables+1):
                if c < nvariables:
                    result += ecuaciones[f][c] * resultados[niteracion][c]
                else:
                    result += ecuaciones[f][c]
            result = round(result, 4)
            resultado.append(result)
        resultados.append(resultado)

        niteracion += 1
        if niteracion >= 2:
            operacion = 0
            for a in range(nvariables):
                if niteracion <= 2:
                    operacion += round((resultados[niteracion-2][a] - 0)**2, 4)
                else:
                    operacion += round((resultados[niteracion-2][a] - resultados[niteracion-3][a])**2, 4)
            condicion.append(round(math.sqrt(operacion), 4))

        if comprobar(resultados, nvariables, condicion): break

    for n in range(len(condicion)):
        print("k=",n+1, resultados[n], "  E=",condicion[n])
        pass
