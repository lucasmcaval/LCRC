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

def calcula_pontos_sequencia_baixa(lista):
    sequencia = 1
    maior_sequencia = 1
    lista = list(set(lista))
    lista.sort()
    for i in range(len(lista) - 1):
        if lista[i + 1] == lista[i] + 1:
            sequencia += 1
        else:
            if sequencia > maior_sequencia:
                maior_sequencia = sequencia
            sequencia = 1
            
    if sequencia >= 4 or maior_sequencia >= 4:
        return 15
    else: 
        return 0
    
def calcula_pontos_sequencia_alta (lista):
    sequencia = 1
    maior_sequencia = 1
    lista = list(set(lista))
    lista.sort()
    for i in range(len(lista) - 1):
        if lista[i + 1] == lista[i] + 1:
            sequencia += 1
            if sequencia > maior_sequencia:
                    maior_sequencia = sequencia
        else:
            sequencia = 1
            
    if sequencia >= 5 or maior_sequencia >= 5:
        return 30
    else: 
        return 0
    
def calcula_pontos_full_house(lista):
    Trinca = False
    Par = False
    for valor in lista:
        if lista.count(valor) == 3:
            Trinca = True
        if lista.count(valor) == 2:
            Par = True
    if Trinca == True and Par == True:
        return calcula_pontos_soma(lista)
    else:
        return 0

def calcula_pontos_quadra (lista):
    quadra = False
    for valor in lista:
        if lista.count(valor) >= 4:
            quadra = True
    if quadra == True:
        return calcula_pontos_soma(lista)
    else:
        return 0

def calcula_pontos_quina (lista):
    quina = False
    for valor in lista:
        if lista.count(valor) >= 5:
            quina = True
    if quina == True:
        return 50
    else:
        return 0
    
def calcula_pontos_regra_avancada(lista):
    dic = {
    'cinco_iguais': 0,
    'full_house': 0,
    'quadra': 0,
    'sem_combinacao': 0,
    'sequencia_alta': 0,
    'sequencia_baixa': 0
}
    dic['cinco_iguais'] = calcula_pontos_quina(lista)
    dic['full_house'] = calcula_pontos_full_house(lista)
    dic["quadra"] = calcula_pontos_quadra(lista)
    dic['sem_combinacao'] = calcula_pontos_soma(lista)
    dic['sequencia_alta'] = calcula_pontos_sequencia_alta(lista)
    dic['sequencia_baixa'] = calcula_pontos_sequencia_baixa(lista)
    
    return dic

def faz_jogada(dados, categoria, cartela):
    pontos_simples = calcula_pontos_regra_simples(dados)
    pontos_avancado = calcula_pontos_regra_avancada(dados)
    if categoria in ['1', '2', '3', '4', '5', '6']:
        categoria_numero = int(categoria)
        cartela['regra_simples'][categoria_numero] = pontos_simples[categoria_numero]
    else:
        cartela['regra_avancada'][categoria] = pontos_avancado[categoria]
    return cartela