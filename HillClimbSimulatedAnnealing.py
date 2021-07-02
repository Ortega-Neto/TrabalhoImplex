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
    return gerarVizinhosAleatorios(nomes, tamanhoDoCaminho)


# Gera uma lista de caminhos aleatórios, vizinhos do caminho atual
def gerarVizinhosAleatorios(caminhoAtual, tamanhoDoCaminho):
    vizinhos = []
    caminho = caminhoAtual

    for i in range(tamanhoDoCaminho):
        vizinhoAleatorio = caminho[random.randint(0, len(caminho) - 1)]
        vizinhos.append(vizinhoAleatorio)
        caminho.remove(vizinhoAleatorio)

    return vizinhos


# Realiza o Calculo da Distancia do caminho, somando todos os valores
# e retorna este resultado
def retornaDistanciaDoCaminho(matrizDasDistancias, caminhoAtual):
    distanciaDoCaminho = 0
    for i in range(len(caminhoAtual) - 1):
        distanciaDoCaminho += matrizDasDistancias[int(caminhoAtual[i]) - 1][int(caminhoAtual[i + 1]) - 1]
    return distanciaDoCaminho


# Gera vizinhos do caminho enviado, por meio de swaps aleatórios
def gerarVizinhosDoCaminhoAtual(caminhoAtual):
    vizinhos = []
    for i in range(len(caminhoAtual)):
        for j in range(i + 1, len(caminhoAtual)):
            vizinho = caminhoAtual.copy()
            vizinho[i] = caminhoAtual[j]
            vizinho[j] = caminhoAtual[i]
            vizinhos.append(vizinho)
    return vizinhos


# Realiza a verificação de qual é o melhor vizinho e retorna ele e
# sua respectiva distância
def retornaOMelhorVizinho(matrizDasDistancias, vizinhos):
    melhorDistancia = retornaDistanciaDoCaminho(matrizDasDistancias, vizinhos[0])
    melhorVizinho = vizinhos[0]

    for vizinho in vizinhos:
        distanciaAtual = retornaDistanciaDoCaminho(matrizDasDistancias, vizinho)

        if distanciaAtual < melhorDistancia:
            melhorDistancia = distanciaAtual
            melhorVizinho = vizinho

    return melhorVizinho, melhorDistancia


# Realiza o calculo do TSP pelo algoritmo do Hill Climb
def hillClimb(matrizDasDistancias, caminhoInicial):
    solucaoAtual = caminhoInicial
    distanciaAtual = retornaDistanciaDoCaminho(matrizDasDistancias, caminhoInicial)

    vizinhos = gerarVizinhosDoCaminhoAtual(solucaoAtual)
    melhorVizinho, melhorDistancia = retornaOMelhorVizinho(matrizDasDistancias, vizinhos)

    while melhorDistancia < distanciaAtual:
        solucaoAtual = melhorVizinho
        distanciaAtual = melhorDistancia
        vizinhos = gerarVizinhosDoCaminhoAtual(solucaoAtual)
        melhorVizinho, melhorDistancia = retornaOMelhorVizinho(matrizDasDistancias, vizinhos)

    return solucaoAtual, distanciaAtual


# Realiza o calculo do TSP pelo algoritmo do Simulated Annealing
def simulatedAnnealing(matrizDasDistancias, caminhoInicial):
    t = input("Insira o t: ")
    t = int(t)
    distancia = input("Insira a distancia: ")
    distancia = int(distancia)
    numeroDeInteracoes = input("Insira a quantidade de interações: ")
    numeroDeInteracoes = int(numeroDeInteracoes)

    solucaoAtual = caminhoInicial
    distanciaAtual = retornaDistanciaDoCaminho(matrizDasDistancias, caminhoInicial)

    for i in range(numeroDeInteracoes):
        t *= distancia
        vizinhos = gerarVizinhosDoCaminhoAtual(solucaoAtual)
        melhorVizinho, melhorDistancia = retornaOMelhorVizinho(matrizDasDistancias, vizinhos)

        if melhorDistancia < distanciaAtual:
            solucaoAtual = melhorVizinho
            distanciaAtual = melhorDistancia
        else:
            x = random.random()
            if x < math.exp((melhorDistancia - distanciaAtual) / t):
                solucaoAtual = melhorVizinho
                distanciaAtual = melhorDistancia

    return solucaoAtual, distanciaAtual


if __name__ == '__main__':
    # Start na contagem do tempo
    inicioHillClimb = datetime.datetime.now()

    matrizInput = realizarLeituraDoInput()
    matrizDasDistancias, tamanhoDoCaminho = gerarMatrizEuclidianaETamanho(matrizInput)

    caminhoInicial = criarCaminhoInicialAleatorio(matrizInput, tamanhoDoCaminho)
    melhorCaminho, melhorDistencia = hillClimb(matrizDasDistancias, caminhoInicial)

    print()
    print("____________________________________________________________________________________________________")
    print("Hill Climb")
    print()
    print("Melhor caminho -> ", melhorCaminho)
    print("Distância deste caminho -> ", melhorDistencia)
    print()

    # Finalização da contagem de tempo
    finalHillClimb = datetime.datetime.now()
    print("Tempo Total de execução do Hill Climb = ", finalHillClimb - inicioHillClimb)
    print()

    inicioSimulatedAnnealing = datetime.datetime.now()
    melhorCaminho, melhorDistencia = simulatedAnnealing(matrizDasDistancias, caminhoInicial)
    print()
    print("____________________________________________________________________________________________________")
    print("Simulated Annealing")
    print()
    print("Melhor caminho -> ", melhorCaminho)
    print("Distância deste caminho -> ", melhorDistencia)
    print()
    # Finalização da contagem de tempo
    finalSimulatedAnnealing = datetime.datetime.now()
    print("Tempo Total de execução do Hill Climb = ", finalSimulatedAnnealing - inicioSimulatedAnnealing)
