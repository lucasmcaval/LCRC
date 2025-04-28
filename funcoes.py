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

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    dados_rolados.append(dados_no_estoque[dado_para_remover])
    dados_no_estoque.pop(dado_para_remover)
    lista = [dados_rolados, dados_no_estoque]
    return lista