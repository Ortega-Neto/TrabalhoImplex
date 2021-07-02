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
            x = float(vertice[1]) - float(verticeParaCalcular[1])
            x = x * x
            y = float(vertice[2]) - float(verticeParaCalcular[2])
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
        distancia += matrizDeDistancias[int(caminho[i]) - 1][int(caminho[i + 1]) - 1]
    return distancia


def gerarVizinhos(caminho):
    vizinhos = []
    for i in range(len(caminho)):
        for j in range(i + 1, len(caminho)):
            vizinho = caminho.copy()
            vizinho[i] = caminho[j]
            vizinho[j] = caminho[i]
            vizinhos.append(vizinho)
    return vizinhos


def calcularMelhorVizinho(vizinhos):
    melhorDistancia = 1000000000000000
    melhorVizinho = []

    for vizinho in vizinhos:
        distanciaAtual = calcularADistanciaDaRota(vizinho)

        if distanciaAtual < melhorDistancia:
            melhorDistancia = distanciaAtual
            melhorVizinho = vizinho

    return melhorVizinho, melhorDistancia


def simulatedAnnealing(caminhoInicial, distanciaInicial, interacoes, t, distancia):
    solucaoAtual = caminhoInicial
    distanciaAtual = distanciaInicial

    for i in range(interacoes):
        t *= distancia
        vizinhos = gerarVizinhos(caminhoInicial)
        melhorVizinho, melhorDistancia = calcularMelhorVizinho(vizinhos)

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
    interacoes = input("Insira uma quantidade de interações: ")
    t = input("Insira um t: ")
    distancia = input("Insira uma distancia: ")

    # Inicio de contagem de tempo
    inicio = datetime.datetime.now()

    # Leitura dos Arquivos e criação das variáveis
    matrizDeVertices = leArquivoTxt()

    # Criação da Matriz das Distâncias
    calcularAsDistanciasEntreOsVertices()

    # Caminho Inicial, ordem de inserção
    caminhoInicial = retornaNomeDosVertices()

    # Inicialização das variáveis para o calculo co Hill Climb
    caminho = gerarCaminhoAleatorio(caminhoInicial)
    distanciaDaRota = calcularADistanciaDaRota(caminho)

    # Calculo do Simulated Annealing
    solucao, distancia = simulatedAnnealing(caminho, distanciaDaRota, int(interacoes), float(t), int(distancia))
    print("Solucao ", solucao)
    print("Distancia Solucao " + "{:.2f}".format(distancia))

    # Finalização da contagem de tempo
    final = datetime.datetime.now()
    print("tempo de execução", final - inicio)
