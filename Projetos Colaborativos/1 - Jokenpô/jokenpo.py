# Jokenpô
# Pedra, Papel ou Tesoura

# Importa a biblioteca tabulate
from tabulate import tabulate

# Importa a biblioteca random
import random as rd

# Importa a biblioteca getpass
import getpass

# ENTRADA

# Boas-vindas
print("\nBem-vindo ao Jokenpô! Aqui você jogará Pedra, Papel e Tesoura contra seus oponentes. Escolha uma das modalidades:\n")

# Dicionário das modalidades
modalidades = {
    1: "Humano x Computador",
    2: "Humano x Humano",
    3: "Computador x Computador"
}

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

# Impressão da escolha da modalidade do jogo
print(f"\nModo de jogo: {modalidades[modo_de_jogo]}.")

# Definição dos jogadores

if modo_de_jogo in [1, 2]:

    jogador = input("Defina o nome do jogador 1: ")
    jogador_2 = input("Defina o nome do jogador 2: ")

else:
    jogador, jogador_2 = "Máquina 1", "Máquina 2"

# Impressão dos jogadores
print(f"Jogadores: {jogador} e {jogador_2}.\n")

# PROCESSAMENTO

# Dicionário das ações
acoes = {
        0: "Pedra",
        1: "Papel",
        2: "Tesoura"
    }

escolha_jogador = 0 # Ação do jogador
escolha_jogador_2 = 0 # Ação do jogador_2

# Lista do Placar
placar = [
    ["Rodada", jogador, jogador_2]
]

cont_rodada = 0 # Contador da rodada
point_jogador = 0 # Pontuação do jogador 1
point_jogador_2 = 0 # Pontuação do jogador 2

# Função que inicia o jogo
def iniciar_jogo(modo, contador, p1, p2): # p1 - Pontuação do jogador 1 e p2 - Pontuação do jogador 2

    # Exibe as opções de jogada
    if modo != 3:
        print("Opções: \n")
        for key, value in acoes.items():
            print(f"Digite {key} para {value}")
    
    # Exibe as regras do jogo
    print("\nRegras: Pedra ganha da tesoura / Tesoura ganha do papel / Papel ganha da pedra\n")

    # Começa a rodada
    return rodada(modo, contador, p1, p2)

# Função da rodada
def rodada(modo, contador, p1, p2):

    while True:
        
        p1, p2 = acao_jogador(modo, p1, p2)  # Captura os valores atualizados
        contador = update_placar(contador, p1, p2)  # Captura a contagem atualizada

        continuar = int(input("\nDeseja(m) continuar? (1-sim e 2-não) ")) # Pergunta para continuar

        if continuar == 2:
            break
    
    # Exibe o placar
    print(f"\nResultado: {definir_ganhador(p1, p2)}")
    print("\nPlacar")
    print(tabulate(placar, tablefmt="fancy_grid"))

# Função da ação do jogador
def acao_jogador(modo, p1, p2):
    global escolha_jogador, escolha_jogador_2  # Usa as variáveis globais definidas antes
    texto = "digite uma ação (Pedra, Papel ou Tesoura):"

    # Inputs dos jogadores
    if modo == 1:
        escolha_jogador = int(input(f"\n{jogador}, {texto} "))
        escolha_jogador_2 = rd.randrange(0, 3)
    
    elif modo == 2:
        escolha_jogador = int(getpass.getpass(f"\n{jogador}, {texto} "))
        escolha_jogador_2 = int(getpass.getpass(f"\n{jogador_2}, {texto} "))

    else:
        escolha_jogador = rd.randrange(0, 3)
        escolha_jogador_2 = rd.randrange(0, 3)

    # Lógica do jogo
    if escolha_jogador == escolha_jogador_2:
        p1 += 1
        p2 += 1
        print("\nEmpate!")

    elif (escolha_jogador == 0 and escolha_jogador_2 == 2) or \
         (escolha_jogador == 1 and escolha_jogador_2 == 0) or \
         (escolha_jogador == 2 and escolha_jogador_2 == 1):
        p1 += 1
        print(f"\n{jogador} venceu!")

    else:
        p2 += 1
        print(f"\n{jogador_2} venceu!")
    
    return p1, p2  # Retorna os valores atualizados

# Função para atualizar o placar do jogo
def update_placar(contador, p1, p2):

    contador += 1  # Atualiza o número da rodada
    placar.append([f"{contador}ª", p1, p2])  # Adiciona ao placar
    return contador  # Retorna o contador atualizado

# Função para definir o ganhador
def definir_ganhador(p1, p2):

    global jogador, jogador_2

    if p1 == p2:
        print(f"empate.")
    elif p1 > p2:
        print(f"o jogador {jogador} ganhou.")
    else:
        print(f"o jogador {jogador_2} ganhou.")

# SAÍDA

# Chama a função para iniciar o jokenpô
iniciar_jogo(modo_de_jogo, cont_rodada, point_jogador, point_jogador_2)
