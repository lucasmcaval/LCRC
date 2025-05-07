from funcoes import *

def cartela_valida(categoria, cartela):
    if categoria in ['1','2','3','4','5','6']:
        categoria = int(categoria)

    if categoria in cartela['regra_simples'] and cartela['regra_simples'][categoria] != -1:
        return "CHEIO"
    
    elif categoria in cartela['regra_avancada'] and cartela['regra_avancada'][categoria] != -1:
        return "CHEIO"
    
    elif categoria not in cartela['regra_avancada'] and categoria not in cartela['regra_simples']:
       return "INVALIDO"

dados_rolados = rolar_dados(5)
dados_guardados = []

cartela = {
    'regra_simples': {
        1: -1,
        2: -1,
        3: -1,
        4: -1,
        5: -1,
        6: -1
    },
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

def rodada(cartela, dados_rolados, dados_guardados):
    conta_rerrol = 0
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    resposta = input()

    while resposta != "0":

        if resposta == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())

            dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, indice)

            print(f'Dados rolados: {dados_rolados}')
            print(f'Dados guardados: {dados_guardados}')

            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            resposta = input()

        elif resposta == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())

            dados_rolados, dados_guardados = remover_dado(dados_rolados, dados_guardados, indice)

            print(f'Dados rolados: {dados_rolados}')
            print(f'Dados guardados: {dados_guardados}')

            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            resposta = input()

        elif resposta == "3":
            if conta_rerrol >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                dados_rolados = rolar_dados(len(dados_rolados))
                conta_rerrol += 1

            print(f'Dados rolados: {dados_rolados}')
            print(f'Dados guardados: {dados_guardados}')

            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            resposta = input()

        elif resposta == '4':
            imprime_cartela(cartela)

            print(f'Dados rolados: {dados_rolados}')
            print(f'Dados guardados: {dados_guardados}')

            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            resposta = input()

        else:
            print("Opção inválida. Tente novamente.")
            resposta = input()
    
    dados = dados_guardados + dados_rolados

    print("Digite a combinação desejada:")
    categoria = input()

    validacao = cartela_valida(categoria, cartela)

    while validacao == "CHEIO" or validacao == 'INVALIDO':
        if validacao == "CHEIO":
            print("Essa combinação já foi utilizada.")
            categoria = input()

        elif validacao == "INVALIDO":
            print("Combinação inválida. Tente novamente.")
            categoria = input()

        validacao = cartela_valida(categoria, cartela)

    faz_jogada(dados, categoria, cartela)

    return cartela

rodadas = 0

imprime_cartela(cartela)
print(f'Dados rolados: {dados_rolados}')
print(f'Dados guardados: {dados_guardados}')

while rodadas < 12:
    cartela = rodada(cartela, dados_rolados, dados_guardados)
    
    dados_rolados = rolar_dados(5)
    dados_guardados = []

    if rodadas != 11:
        print(f'Dados rolados: {dados_rolados}')
        print(f'Dados guardados: {dados_guardados}')
    
    rodadas += 1

soma_simples = sum(v for v in cartela['regra_simples'].values() if v != -1)

soma_avancada = sum(v for v in cartela['regra_avancada'].values() if v != -1)

pontuacao_total = soma_simples + soma_avancada
if soma_simples >= 63:
    pontuacao_total += 35


imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao_total}")