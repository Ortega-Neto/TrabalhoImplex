import math
import datetime
import random

matrizDeDistancias = []  # Matriz que contém as distâncias
matrizDeVertices = []
tamanhoDaMatriz = []


def leArquivoTxt():
    arquivo = open("entrada.txt", "r")
    return transformaEmVetor(arquivo)


def transformaEmVetor(arquivo):
    linhas = arquivo.readlines()
    matrizLida = []

    for elemento in linhas:
        matrizLida.append(elemento.split())

    arquivo.close()
    return matrizLida


def calcularAsDistanciasEntreOsVertices():
    i = 0
    for vertice in matrizDeVertices:
        distancia = []
        for verticeParaCalcular in matrizDeVertices:
            x = int(vertice[1]) - int(verticeParaCalcular[1])
            x = x * x
            y = int(vertice[2]) - int(verticeParaCalcular[2])
            y = y * y
            distancia.append(math.sqrt(x + y))
        matrizDeDistancias.append(distancia)
        i += 1
    tamanhoDaMatriz.append(i)


def retornaNomeDosVertices():
    nomes = []
    for vertice in matrizDeVertices:
        nomes.append(vertice[0])
    return nomes


# def calcularTamanhoDaMatriz():
#     i = 0
#     for vertice in matrizDeVertices:
#         i += 1
#     return i


def gerarCaminhoAleatorio(caminhoAtual):
    solucao = []
    cidades = caminhoAtual

    for i in range(tamanhoDaMatriz[0]):
        caminhoAleatorio = cidades[random.randint(0, len(cidades) - 1)]
        solucao.append(caminhoAleatorio)
        cidades.remove(caminhoAleatorio)

    return solucao


def calcularADistanciaDaRota(caminho):
    distancia = 0
    for i in range(len(caminho) - 1):
        print(int(caminho[i]))
        print(int(caminho[i+1]))
        distancia += matrizDeDistancias[int(caminho[i]) - 1][int(caminho[i + 1]) - 1]
    print(distancia)
    return distancia


def hillClimb(funcaoCusto):
    print(matrizDeDistancias)


if __name__ == '__main__':
    inicio = datetime.datetime.now()

    matrizDeVertices = leArquivoTxt()
    caminhoInicial = retornaNomeDosVertices()
    calcularAsDistanciasEntreOsVertices()
    # hillClimb(10)

    # gerarCaminhoAleatorio(caminhoInicial)

    calcularADistanciaDaRota(caminhoInicial)

    final = datetime.datetime.now()
    print("tempo de execução", final - inicio)
