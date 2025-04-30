# Jokenpô - Pedra, Papel ou Tesoura

import random as rd # Biblioteca para importar números aleatórios
import getpass # Biblioteca para ocultar a resposta do input no terminal
from tabulate import tabulate # Biblioteca para criar tabelas no terminal

# Dicionário das modalidades
modalidades = {
    1: "Humano x Computador",
    2: "Humano x Humano",
    3: "Computador x Computador"
}

# Dicionário das ações
acoes = {
    0: "Pedra",
    1: "Papel",
    2: "Tesoura"
}

# Função para iniciar o jogo
def iniciar():

    # Boas-vindas
    print("\nBem-vindo ao Jokenpô!\nEscolha uma das modalidades:\n")

    modo = escolher_modo() # Variável definida pelo resultado da função escolher_modo
    jogadores = definir_jogadores(modo) # Variável definida pelo resultado da função definir_jogadores

    # Impressão das regras do jogo
    print("\nRegras: Pedra vence Tesoura, Tesoura vence Papel, Papel vence Pedra.\n")

    # Condição: se o modo for diferente de três, imprimi as opções, pois no modo 3 é computador x computador
    if modo != 3:
        print("Opções:")

        # Laço FOR para percorrer o dic. acoes e imprimir cada opção
        for key, value in acoes.items():
            print(f"Digite {key} para {value}")

    # Chama a função rodada 
    rodada(modo, jogadores)

# Função para escolher o modo de jogo
def escolher_modo():

    # Laço FOR para percorrer dic. modalidades para imprimir cada modalidade
    for key, value in modalidades.items():
        print(f"{key}. {value}")

    # Loop WHILE verdadeiro, se o usuário não digitar uma das modalidades, não sai do loop
    while True:

        # Defini a variável modo para o resultado do input
        modo = int(input("\nEscolha a modalidade (1, 2 ou 3): "))

        
        # Condição: se o modo é um valor que está em modalidades, 
        # imprimi a modalidade escolhida e retorna a variável modo.
        # Se não, imprimi "Opção inválida! Tente novamente." e continua o loop

        if modo in modalidades:
            print(f"\nModo de jogo: {modalidades[modo]}.")
            return modo
        else:
            print("Opção inválida! Tente novamente.")

# Função para definir os jogadores
def definir_jogadores(modo):

    # Dicionário dos jogadores
    jogadores = {
        1: ["", 0],  # [Nome, Pontos]
        2: ["", 0]
    }

    # Condição: se o modo é um valor da lista, defini os nomes dos jogadores.
    # Se não, os nomes dos jogadores 1 e 2 é: máquina 1 e máquina 2, respectivamente.
    if modo in [1, 2]:
        jogadores[1][0] = input("Defina o nome do jogador 1: ").strip().lower()

        # Condição: se o modo é igual a 2, defini o nome do jogador 2 como "Computador"
        jogadores[2][0] = input("Defina o nome do jogador 2: ").strip().lower() if modo == 2 else "Computador"
    else:
        jogadores[1][0], jogadores[2][0] = "Máquina 1", "Máquina 2"

    # Imprimi os nomes dos jogadores
    print(f"\nJogadores: {jogadores[1][0]} e {jogadores[2][0]}.\n")

    return jogadores # Retorna jogadores

# Função principal para rodadas do jogo
def rodada(modo, jogadores):

    contador = 0 # Defini a variável contador, usada para contar as rodadas

    # Variável do placar que é uma lista com listas dentro
    placar = [["Rodada", jogadores[1][0], jogadores[2][0]]]

    # Loop WHILE verdadeiro, é encerrado quando o(s) jogador(es) decidir(em) terminar o jogo
    while True:

        contador += 1 # Atualiza a rodada
        print(f"\n----{contador}ª Rodada----") # Imprimi a rodada referente
        jogar(modo, jogadores) # Chama a função para jogar

        # Atualiza o placar
        placar.append([f"{contador}ª", jogadores[1][1], jogadores[2][1]])

        # Pergunta para continuar 
        continuar = input("\nDeseja(m) continuar? (s para sim ou n para não): ").strip().lower()
        
        # Defini continuar como o valor retornado de verificador
        continuar = verificador(continuar)

        # Condição: se continuar for falso, chama a função encerrar e encerra o loop WHILE
        if not continuar:
            encerrar(jogadores, placar)
            break

# Função para verificar se o jogo continua
def verificador(valor):

    while valor not in ["n", "s"]: # enquanto o valor colocado pelo usuário for diferente dos ultilizados na execução

        print("\nValor Inválido!")
        valor = input("\nDeseja(m) continuar? (s para sim ou n para não): ").strip().lower() # pergunta ao usuário se quer continuar o jogo

    if valor == "n":
        return False # se for falso, o loop quebrará e encerrará o jogo
    elif valor == "s":
        return True

# Função para realizar a jogada
def jogar(modo, jogadores):

    texto = "escolha (0: Pedra, 1: Papel, 2: Tesoura): " 

    # as escolhas de cada jogador são iniciadas
    escolha_1 = None 
    escolha_2 = None

    while True:

        try:
            if modo == 1:
                escolha_1 = int(input(f"\n{jogadores[1][0]}, {texto}"))
                if escolha_1 not in acoes:
                    raise ValueError # se der erro, manda para a contenção
                
                escolha_2 = rd.randint(0, 2) # jogada do computador, ultilizando a aleatoriedade da random
            # se o modo for humano contra humano, ultiliza a biblioteca getpass para ocultar cada jogada de cada jogador
            elif modo == 2:
                escolha_1 = int(getpass.getpass(f"\n{jogadores[1][0]}, {texto}"))
                escolha_2 = int(getpass.getpass(f"\n{jogadores[2][0]}, {texto}"))
                
                if escolha_1 not in acoes or escolha_2 not in acoes:
                    raise ValueError
            # se o modo for computador contra computador, ultilizamos duas random para o sorteio de jogadas
            else:
                escolha_1 = rd.randint(0, 2) 
                escolha_2 = rd.randint(0, 2)

            break # quebra o loop
        # ultiliza o try e except para a contenção de erros
        except ValueError:
            print("Entrada inválida! Escolha 0, 1 ou 2.")

    print(f"\n{jogadores[1][0]} escolheu {acoes[escolha_1]}") # Escolha do jogador 1
    print(f"{jogadores[2][0]} escolheu {acoes[escolha_2]}") # Escolha do jogador 2

    # Lógica do jogo
    if escolha_1 == escolha_2:
        print("\nEmpate!")

    elif (escolha_1 == 0 and escolha_2 == 2) or \
         (escolha_1 == 1 and escolha_2 == 0) or \
         (escolha_1 == 2 and escolha_2 == 1):
        jogadores[1][1] += 1
        print(f"\n{jogadores[1][0]} venceu!")

    else:
        jogadores[2][1] += 1
        print(f"\n{jogadores[2][0]} venceu!")

# Função para encerrar o jogo e mostrar o placar
def encerrar(jogadores, placar):

    if jogadores[1][1] == jogadores[2][1]: # se a jogada de cada um for igual, dá empate e ninguém pontua
        resultado = "Empate."

    elif jogadores[1][1] > jogadores[2][1]: # se a jogada do primeiro jogador for maior, ele pontua 1
        resultado = f"{jogadores[1][0]} ganhou!"

    else:
        resultado = f"{jogadores[2][0]} ganhou!" # se não, o jogador 2 pontua 1

    print(f"\nResultado final: {resultado}\n") # mostra o resultado com separação de linhas
    print(tabulate(placar, headers="firstrow", tablefmt="fancy_grid")) # mostra a tabela utilizando a biblioteca tabulate com suas especificações

# Executa o jogo
iniciar()

# Agradecimentos
print("\n Obrigado por jogar!")
print("\n Desenvolvido por: Libia Silveira, Pedro Fonseca e Sérgio Calazans.\n")