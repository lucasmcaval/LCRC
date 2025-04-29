from funcoes import *
validos = ["0", "1", "2", "3", "4"]
cartela = {
    'regra_simples':  {
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

dados_guardados = []
imprime_cartela(cartela)
rodadas = 0

while rodadas < 12:

    dados_rolados = rolar_dados(5 - len(dados_guardados))
    rerrol = 0
    while True:
        print(f"Dados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_guardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        resposta = input("")
        if resposta not in validos:
            print("Opção inválida. Tente novamente.")
            continue

        elif resposta == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = input("")
            if indice in [str(i) for i in range(len(dados_rolados))]:
                dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, int(indice))
            else:
                print("Opção inválida. Tente novamente.")
            
        elif resposta == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = input("")
            if indice in [str(i) for i in range(len(dados_guardados))]:
                dados_rolados, dados_guardados = remover_dado(dados_rolados, dados_guardados, int(indice))
            else:
                print("Índice inválido. Tente novamente.")

        elif resposta == "3":
            if rerrol < 2:
                rerrol += 1
                dados_rolados = rolar_dados(5 - len(dados_guardados))
            else:
                print("Você já usou todas as rerrolagens.")

        elif resposta == "4":
            imprime_cartela(cartela)
        
        elif resposta == "0":
            dados_final = dados_guardados + dados_rolados
            imprime_cartela(cartela)
            print("Digite a combinação desejada:")
            jogada_valida = False
            while jogada_valida == False:
                categoria = input("")
                if categoria in ["1", "2", "3", "4", "5", "6"]:
                    if cartela['regra_simples'][int(categoria)] == -1:
                        cartela = faz_jogada(dados_final, categoria, cartela)
                        jogada_valida = True
                    else:
                        print("Essa combinação já foi utilizada.")
                elif categoria in cartela['regra_avancada']:
                    if cartela['regra_avancada'][categoria] == -1:
                        cartela = faz_jogada(dados_final, categoria, cartela)
                        jogada_valida = True
                    else:
                        print("Essa combinação já foi utilizada.")
                else:
                    print("Combinação inválida. Tente novamente.")
            break 

    dados_guardados = []
    rodadas += 1

imprime_cartela(cartela)

pontuacao_total = 0

for i in range(1, 7):
    valor = cartela["regra_simples"][i]
    if valor != -1:
        pontuacao_total += valor

for chave in cartela["regra_avancada"]:
    valor = cartela["regra_avancada"][chave]
    if valor != -1:
        pontuacao_total += valor

print(f"Pontuação total: {pontuacao_total}")
