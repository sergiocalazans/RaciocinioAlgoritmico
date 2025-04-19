import tkinter as tk
import random
from tkinter import simpledialog, messagebox

# Opções do jogo
opcoes = {0: "Pedra", 1: "Papel", 2: "Tesoura"}
modalidades = {1: "Humano x Computador", 2: "Humano x Humano", 3: "Computador x Computador"}

# Placar
pontos_jogador1 = 0
pontos_jogador2 = 0
modo_jogo = 1  # Modo padrão: Humano vs Computador


def escolher_modo():
    """Abre um diálogo para escolher a modalidade do jogo."""
    global modo_jogo
    modo_jogo = simpledialog.askinteger("Modo de Jogo", "Escolha o modo:\n1 - Humano x Computador\n2 - Humano x Humano\n3 - Computador x Computador", minvalue=1, maxvalue=3)
    if modo_jogo not in [1, 2, 3]:
        messagebox.showerror("Erro", "Modo inválido! Escolha 1, 2 ou 3.")
        escolher_modo()
    else:
        lbl_modo.config(text=f"Modo Selecionado: {modalidades[modo_jogo]}")


def jogar(escolha_jogador1=None):
    """Executa uma jogada baseada no modo de jogo."""
    global pontos_jogador1, pontos_jogador2

    # Determina a jogada do segundo jogador
    if modo_jogo == 1:
        escolha_jogador2 = random.randint(0, 2)  # Computador escolhe
    elif modo_jogo == 2:
        escolha_jogador2 = simpledialog.askinteger("Jogador 2", "Jogador 2, escolha:\n0 - Pedra\n1 - Papel\n2 - Tesoura", minvalue=0, maxvalue=2)
        if escolha_jogador2 not in opcoes:
            messagebox.showerror("Erro", "Escolha inválida! Tente novamente.")
            return
    else:
        escolha_jogador1 = random.randint(0, 2)
        escolha_jogador2 = random.randint(0, 2)

    # Define o vencedor
    if escolha_jogador1 == escolha_jogador2:
        resultado = "Empate!"
    elif (escolha_jogador1 == 0 and escolha_jogador2 == 2) or \
         (escolha_jogador1 == 1 and escolha_jogador2 == 0) or \
         (escolha_jogador1 == 2 and escolha_jogador2 == 1):
        resultado = "Jogador 1 venceu!"
        pontos_jogador1 += 1
    else:
        resultado = "Jogador 2 venceu!"
        pontos_jogador2 += 1

    # Atualiza o rótulo do placar
    lbl_resultado.config(text=f"Jogador 1 escolheu: {opcoes[escolha_jogador1]}\nJogador 2 escolheu: {opcoes[escolha_jogador2]}\n{resultado}")
    lbl_placar.config(text=f"Placar - Jogador 1: {pontos_jogador1} | Jogador 2: {pontos_jogador2}")


# Criando a janela principal
janela = tk.Tk()
janela.title("Jokenpô")
janela.geometry("350x450")
janela.resizable(False, False)

# Botão para escolher a modalidade
btn_modo = tk.Button(janela, text="Escolher Modo", font=("Arial", 12), command=escolher_modo)
btn_modo.pack(pady=10)

lbl_modo = tk.Label(janela, text="Modo Selecionado: Humano x Computador", font=("Arial", 12), fg="blue")
lbl_modo.pack(pady=5)

# Botões de escolha para o jogador 1
lbl_instrucao = tk.Label(janela, text="Jogador 1, escolha sua jogada:", font=("Arial", 12))
lbl_instrucao.pack(pady=5)

btn_pedra = tk.Button(janela, text="Pedra", font=("Arial", 12), width=10, command=lambda: jogar(0))
btn_papel = tk.Button(janela, text="Papel", font=("Arial", 12), width=10, command=lambda: jogar(1))
btn_tesoura = tk.Button(janela, text="Tesoura", font=("Arial", 12), width=10, command=lambda: jogar(2))

btn_pedra.pack(pady=5)
btn_papel.pack(pady=5)
btn_tesoura.pack(pady=5)

# Exibição do resultado
lbl_resultado = tk.Label(janela, text="", font=("Arial", 12), fg="blue")
lbl_resultado.pack(pady=20)

# Placar
lbl_placar = tk.Label(janela, text="Placar - Jogador 1: 0 | Jogador 2: 0", font=("Arial", 12), fg="green")
lbl_placar.pack(pady=10)

# Executa o loop da interface gráfica
janela.mainloop()
