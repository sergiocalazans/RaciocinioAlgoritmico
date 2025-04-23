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

        # Loop FOR para percorrer o dic. acoes e imprimir cada opção
        for key, value in acoes.items():
            print(f"Digite {key} para {value}")

    # Chama a função rodada 
    rodada(modo, jogadores)

# Função para escolher o modo de jogo
def escolher_modo():

    # Loop FOR para percorrer dic. modalidades para imprimir cada modalidade
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
        1: ["", 0, 0],  # [Nome, Escolha, Pontos]
        2: ["", 0, 0]
    }

    # Condição: se o modo é um valor da lista, defini os nomes dos jogadores.
    # Se não, os nomes dos jogadores 1 e 2 é: máquina 1 e máquina 2, respectivamente.
    if modo in [1, 2]:
        jogadores[1][0] = input("Defina o nome do jogador 1: ")

        # Condição: se o modo é igual a 2, defini o nome do jogador 2 como "Computador"
        jogadores[2][0] = input("Defina o nome do jogador 2: ") if modo == 2 else "Computador"
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
        print(f"\n----{contador}ª Rodada----")
        jogar(modo, jogadores)
        placar.append([f"{contador}ª", jogadores[1][2], jogadores[2][2]])

        continuar = input("\nDeseja continuar? (s para sim ou n para não): ").strip().lower()
        
        while continuar not in ["n", "s"]:

            print("\nValor Inválido!")
            continuar = input("\nDeseja continuar? (s para sim ou n para não): ").strip().lower()

            if continuar == "n":
                encerrar(jogadores, placar)
                return False
            else:
                break
            


# Função para realizar a jogada
def jogar(modo, jogadores):

    texto = "escolha (0: Pedra, 1: Papel, 2: Tesoura): "

    while True:

        try:
            if modo == 1:
                jogadores[1][1] = int(input(f"\n{jogadores[1][0]}, {texto}"))
                
                if jogadores[1][1] not in acoes:
                    raise ValueError
                
                jogadores[2][1] = rd.randint(0, 2)

            elif modo == 2:
                jogadores[1][1] = int(getpass.getpass(f"\n{jogadores[1][0]}, {texto}"))
                jogadores[2][1] = int(getpass.getpass(f"\n{jogadores[2][0]}, {texto}"))
                
                if jogadores[1][1] not in acoes or jogadores[2][1] not in acoes:
                    raise ValueError
                
            else:
                jogadores[1][1] = rd.randint(0, 2)
                jogadores[2][1] = rd.randint(0, 2)
            break

        except ValueError:
            print("Entrada inválida! Escolha 0, 1 ou 2.")

    print(f"\n{jogadores[1][0]} escolheu {acoes[jogadores[1][1]]}")
    print(f"{jogadores[2][0]} escolheu {acoes[jogadores[2][1]]}")

    if jogadores[1][1] == jogadores[2][1]:
        print("\nEmpate!")

    elif (jogadores[1][1] == 0 and jogadores[2][1] == 2) or \
         (jogadores[1][1] == 1 and jogadores[2][1] == 0) or \
         (jogadores[1][1] == 2 and jogadores[2][1] == 1):
        jogadores[1][2] += 1
        print(f"\n{jogadores[1][0]} venceu!")

    else:
        jogadores[2][2] += 1
        print(f"\n{jogadores[2][0]} venceu!")

# Função para encerrar o jogo e mostrar o placar
def encerrar(jogadores, placar):

    if jogadores[1][2] == jogadores[2][2]:
        resultado = "Empate."

    elif jogadores[1][2] > jogadores[2][2]:
        resultado = f"{jogadores[1][0]} ganhou!"

    else:
        resultado = f"{jogadores[2][0]} ganhou!"

    print(f"\nResultado final: {resultado}\n")
    print(tabulate(placar, headers="firstrow", tablefmt="fancy_grid"))

# Executa o jogo
iniciar()
