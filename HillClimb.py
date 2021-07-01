# Alunos: Luiz Carlos Ortega Neto
#         RGA:2020.1906.011-3
#         Curso: Engenharia de Software
#         Rodolfo Miguel Alves dos Santos
#         RGA: 2017.1906.118-1
#         Curso: Engenharia de Software

import math
import datetime
import random

# Realiza a leitura do arquivo input e chama a
# função transformarInputEmMatriz() para transformar em matriz
def realizarLeituraDoInput():
    input = open("input.txt", "r")
    return transformarInputEmMatriz(input)


# Realiza a transformação do que foi lido no arquivo em uma matriz
def transformarInputEmMatriz(input):
    linhas = input.readlines()
    matrizInput = []

    for l in linhas:
        matrizInput.append(l.split())

    input.close()
    return matrizInput


# Gera a matriz fazendo calculo da distância euclidiana e salvando
# as distancias de todos os vertices. Retorna essa matriz e o seu tamanho
def gerarMatrizEuclidianaETamanho(matrizInput):
    matrizDasDistancias = []
    i = 0
    for verticeX in matrizInput:
        distancia = []
        for verticeY in matrizInput:
            x = int(verticeX[1]) - int(verticeY[1])
            x = pow(x, 2)
            y = int(verticeX[2]) - int(verticeY[2])
            y = pow(y, 2)
            distancia.append(math.sqrt(x + y))
        matrizDasDistancias.append(distancia)
        i += 1
    lengthDaMatriz = i
    return matrizDasDistancias, lengthDaMatriz


# Gera um caminho aleatório inicial, baseado nos números dos vertices
def criarCaminhoInicialAleatorio(matrizInput, tamanhoDoCaminho):
    nomes = []
    for vertice in matrizInput:
        nomes.append(vertice[0])
    return gerarCaminhosAleatoriosVizinhos(nomes, tamanhoDoCaminho)


# Gera uma lista de caminhos aleatórios, vizinhos do caminho atual
def gerarCaminhosAleatoriosVizinhos(caminhoAtual, tamanhoDoCaminho):
    vizinhos = []
    caminho = caminhoAtual

    for i in range(tamanhoDoCaminho):
        vizinhoAleatorio = caminho[random.randint(0, len(caminho) - 1)]
        vizinhos.append(vizinhoAleatorio)
        caminho.remove(vizinhoAleatorio)

    return vizinhos


def retornaDistanciaDoCaminho(matrizDasDistancias, caminho):
    distanciaDoCaminho = 0
    for i in range(len(caminho) - 1):
        distanciaDoCaminho += matrizDasDistancias[int(caminho[i]) - 1][int(caminho[i + 1]) - 1]
    return distanciaDoCaminho


def gerarVizinhos(caminho):
    vizinhos = []
    for i in range(len(caminho)):
        for j in range(i + 1, len(caminho)):
            vizinho = caminho.copy()
            vizinho[i] = caminho[j]
            vizinho[j] = caminho[i]
            vizinhos.append(vizinho)
    return vizinhos


def calcularMelhorVizinho(matrizDasDistancias, vizinhos):
    melhorDistancia = 1000000000000000
    melhorVizinho = []

    for vizinho in vizinhos:
        distanciaAtual = retornaDistanciaDoCaminho(matrizDasDistancias, vizinho)

        if distanciaAtual < melhorDistancia:
            melhorDistancia = distanciaAtual
            melhorVizinho = vizinho

    return melhorVizinho, melhorDistancia


def hillClimb(matrizDasDistancias, caminhoInicial):
    solucaoAtual = caminhoInicial
    distanciaAtual = retornaDistanciaDoCaminho(matrizDasDistancias, caminhoInicial)

    vizinhos = gerarVizinhos(caminhoInicial)
    melhorVizinho, melhorDistancia = calcularMelhorVizinho(matrizDasDistancias, vizinhos)

    while melhorDistancia < distanciaAtual:
        solucaoAtual = melhorVizinho
        distanciaAtual = melhorDistancia
        vizinhos = gerarVizinhos(solucaoAtual)
        melhorVizinho, melhorDistancia = calcularMelhorVizinho(matrizDasDistancias, vizinhos)

    return solucaoAtual, distanciaAtual


if __name__ == '__main__':
    # Start na contagem do tempo
    inicio = datetime.datetime.now()

    matrizInput = realizarLeituraDoInput()
    matrizDasDistancias, tamanhoDoCaminho = gerarMatrizEuclidianaETamanho(matrizInput)

    caminhoInicial = criarCaminhoInicialAleatorio(matrizInput, tamanhoDoCaminho)
    print(hillClimb(matrizDasDistancias, caminhoInicial))

    # Finalização da contagem de tempo
    final = datetime.datetime.now()
    print("Tempo Total de execução = ", final - inicio)
