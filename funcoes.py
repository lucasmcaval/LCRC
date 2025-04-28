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

def calcula_pontos_regra_simples (dados_rolados):
    pontuacao_dados = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for dado in dados_rolados:
        for valor_dado in pontuacao_dados.keys():
           if dado == valor_dado:
               pontuacao_dados[valor_dado] += dado
    return pontuacao_dados  

def calcula_pontos_soma(lista):
    pontuacao = 0
    for valor in lista:
        pontuacao += valor
    return pontuacao