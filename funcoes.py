from random import *

def rolar_dados(numero):
    lista = []
    for i in range(numero):
        n = randint(1, 6)
        lista.append(n)
    return lista

def guardar_dado(dados_rolados, dados_guardados, indice):
    dado = dados_rolados.pop(indice)
    dados_guardados.append(dado)
    return [dados_rolados, dados_guardados] 