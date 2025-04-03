# Jokenpô
# Pedra, Papel ou Tesoura

# Importando a biblioteca tabulate

from tabulate import tabulate

# Importando a biblioteca random

import random as rd

# Importando a biblioteca getpass

import getpass

# Entrada

# Dicionário das modalidades
modalidades = {
    1: "Humano x Computador",
    2: "Humano x Humano",
    3: "Computador x Computador"
}

# Boas-vindas
print("\nBem-vindo ao Jokenpô! Aqui você jogará Pedra, Papel e Tesoura contra seus oponentes. Escolha uma das modalidades:\n")

# Laço de repetição da impressão das modalidades
for key, value in modalidades.items():
    print(f"{key}.{value}")

# Entrada da escolha da modalidade
while True: 
    modo_de_jogo = int(input("\nEscolha a modalidade (1, 2 ou 3): "))

    if not modo_de_jogo in [1,2,3]:
        print("Modalidade inválida.")
        continue
    else:
        break
        
print(f"\nModo de jogo: {modalidades[modo_de_jogo]}.")

# Definição dos jogadores
if modo_de_jogo == 2:
    jogador = input("Defina o nome do jogador 1: ")
    jogador_2 = input("Defina o nome do jogador 2: ")

elif modo_de_jogo == 1:
    jogador = input("Defina o nome do jogador: ")
    jogador_2 = "Máquina"

elif modo_de_jogo == 3:
    jogador, jogador_2 = "Máquina 1", "Máquina 2"

print(f"Jogadores: {jogador} e {jogador_2}.\n")

# Processamento

# Dicionário das ações
acoes = {
        0: "Pedra",
        1: "Papel",
        2: "Tesoura"
    }


escolha_jogador = 0 # Ação do jogador
escolha_jogador_2 = 0 # Ação do jogador_2

placar = [
    ["Rodada", jogador, jogador_2],
]

cont_rodada = 0
cont_jogador = 0
cont_jogador_2 = 0

def iniciar_jogo(modo, contador, cont_p1, cont_p2):

    # Exibir as opções e as regras
    if modo != 3:
        print("Opções: \n")
        for key, value in acoes.items():
            print(f"Digite {key} para {value}")
    
    print("\nRegras: Pedra ganha da tesoura / Tesoura ganha do papel / Papel ganha da pedra\n")

    # Começa o jogo
    return jogar(modo, contador, cont_p1, cont_p2)

def jogar(modo, contador, cont_p1, cont_p2):

    while True:
        
        cont_p1, cont_p2 = acao_jogador(modo, cont_p1, cont_p2)  # Captura os valores atualizados
        contador = update_tabela(contador, cont_p1, cont_p2)  # Captura a contagem atualizada

        continuar = int(input("\nDeseja(m) continuar? (1-sim e 2-não) "))

        if continuar == 2:
            break
    
    # Exibir tabela
    print("\nPlacar\n")
    print(tabulate(placar, tablefmt="fancy_grid"))


def acao_jogador(modo, cont_p1, cont_p2):
    global escolha_jogador, escolha_jogador_2  # Usa as variáveis globais definidas antes

    # Seleção dos inputs dos jogadores
    if modo == 1:
        escolha_jogador = int(input("\nDigite uma ação (Pedra, Papel ou Tesoura): "))
        escolha_jogador_2 = rd.randrange(0, 3)
    
    elif modo == 2:
        escolha_jogador = int(getpass.getpass(f"\n{jogador}, digite uma ação (Pedra, Papel ou Tesoura): "))
        escolha_jogador_2 = int(getpass.getpass(f"\n{jogador_2}, digite uma ação (Pedra, Papel ou Tesoura): "))

    else:
        escolha_jogador = rd.randrange(0, 3)
        escolha_jogador_2 = rd.randrange(0, 3)

    # Lógica do jogo
    if escolha_jogador == escolha_jogador_2:
        print("\nEmpate!")

    elif (escolha_jogador == 0 and escolha_jogador_2 == 2) or \
         (escolha_jogador == 1 and escolha_jogador_2 == 0) or \
         (escolha_jogador == 2 and escolha_jogador_2 == 1):
        cont_p1 += 1
        print(f"\n{jogador} venceu!")

    else:
        cont_p2 += 1
        print(f"\n{jogador_2} venceu!")
    
    return cont_p1, cont_p2  # Retorna os valores atualizados


def update_tabela(contador, cont_1, cont_2):
    contador += 1  # Atualiza o número da rodada
    placar.append([f"{contador}ª", cont_1, cont_2])  # Adiciona ao placar
    return contador  # Retorna o contador atualizado


# Saída

iniciar_jogo(modo_de_jogo, cont_rodada, cont_jogador, cont_jogador_2)
