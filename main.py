import numpy
import os

# nvariables = input("Ingrese el numero de variables -> ")

def comprobar(resultados, nvariables):
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
    while True:
        iteracion = []
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
        if comprobar(resultados, nvariables): break


    c = 0
    for r in resultados:
        c += 1
        print(c, r)
