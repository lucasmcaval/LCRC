from funcoes import *

validos = ["0", "1", "2", "3", "4"]

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


imprime_cartela(cartela)

rodadas = 0
while rodadas < 12:
    dados_guardados = []
    rerrolagens = 0
    dados_rolados = rolar_dados(5)

    while True:
        print(f"Dados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_guardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        resposta = input()

        if resposta not in validos:
            print("Opção inválida. Tente novamente.")
            continue

        if resposta == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = input()
            if indice.isdigit() and int(indice) < len(dados_rolados):
                dados_guardados.append(dados_rolados.pop(int(indice)))
            else:
                print("Opção inválida. Tente novamente.")

        elif resposta == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = input()
            if indice.isdigit() and int(indice) < len(dados_guardados):
                dados_rolados.append(dados_guardados.pop(int(indice)))
            else:
                print("Opção inválida. Tente novamente.")

        elif resposta == "3":
            if rerrolagens < 2:
                rerrolagens += 1
                dados_rolados = rolar_dados(5 - len(dados_guardados))
            else:
                print("Você já usou todas as rerrolagens.")

        elif resposta == "4":
            imprime_cartela(cartela)

        else:  
            dados_final = dados_guardados + dados_rolados
            print("Digite a combinação desejada:")
            while True:
                categoria = input()
                
                if categoria in [str(i) for i in range(1, 7)]:
                    num = int(categoria)
                    if cartela['regra_simples'][num] == -1:
                        faz_jogada(dados_final, categoria, cartela)
                        break
                    else:
                        print("Essa combinação já foi utilizada.")
        
                elif categoria in cartela['regra_avancada']:
                    if cartela['regra_avancada'][categoria] == -1:
                        faz_jogada(dados_final, categoria, cartela)
                        break
                    else:
                        print("Essa combinação já foi utilizada.")
                else:
                    print("Combinação inválida. Tente novamente.")
            break

    rodadas += 1


imprime_cartela(cartela)


soma_simples = sum(
    v for v in cartela['regra_simples'].values() if v != -1
)


soma_avancada = sum(
    v for v in cartela['regra_avancada'].values() if v != -1
)

pontuacao_total = soma_simples + soma_avancada
if soma_simples >= 63:
    pontuacao_total += 35

print(f"Pontuação total: {pontuacao_total}")

