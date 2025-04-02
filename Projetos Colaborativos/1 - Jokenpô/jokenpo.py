# Jokenpô
# Pedra, Papel ou Tesoura

# Importando a biblioteca random

import random as rd

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

def iniciar_jogo(modo):

    # Definir as regras
    if modo != 3:
        print("Opções: \n")
        for key, value in acoes.items():
            print(f"Digite {key} para {value}")
    
    print("\nRegras: Pedra ganha da tesoura / Tesoura ganha do papel / Papel ganha da pedra\n")

    # Começa o jogo
    return jogar(modo)

def jogar(modo):

    while True:
        
        acao_jogador(modo)
        
        continuar = int(input("Deseja(m) continuar? (1-sim e 2-não)"))

        if continuar == 2:
            break

        
def acao_jogador(modo):

    if modo == 3:
        escolha_jogador = rd.randrange(0, 2)
        escolha_jogador_2 = rd.randrange(0, 2)

    elif modo == 1:
        escolha_jogador = int(input("\nDigite uma ação(Pedra, Papel ou Tesoura): "))
        escolha_jogador_2 = rd.randrange(0, 2)
    
    if escolha_jogador == escolha_jogador_2:
        return print("\nEmpate!")

    elif (escolha_jogador == 0 and escolha_jogador_2 == 2) or \
            (escolha_jogador == 1 and escolha_jogador_2 == 0) or \
            (escolha_jogador == 2 and escolha_jogador_2 == 2):
        return print(f"\n{jogador} venceu!")

    else:
        return print(f"\n{jogador_2} perdeu!")


# Saída

iniciar_jogo(modo_de_jogo)
