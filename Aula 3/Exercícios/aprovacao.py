# Exercício 5

'''
Escreva um programa que recebe como entrada uma nota e a presença do
aluno. Posteriormente exibe uma mensagem caso o aluno possua presença maior
que 70% e o seu conceito.

Conceito    Nota
 A            Nota maior que 9
 B            Nota maior que 8
 C            Nota maior que 7
 D            Nota maior que 6
 E            Nota maior que 4
 F            Nota menor ou igual a 4

'''

# Entrada 

notaDigitada = float(input("\nDigite sua nota: (max 10, formato: xx.xx) "))
notaDigitada = min(notaDigitada, 10)

presencaDigitada = float(input("Digite sua presença: (max 100, formato: xx.xx) "))
presencaDigitada = min(presencaDigitada, 100)

conceitos = {"A": 10,
            "B": 9,
            "C": 8,
            "D": 7,
            "E": 5,
            "F": 4}

# Processamento

def aprovacao(nota, presenca):

    respostaPresenca = ""
    respostaNota = ""

    if presenca < 70 or nota < 4:
        respostaPresenca = "Reprovado"
    elif nota < 7:
        respostaPresenca = "de Recuperação"
    else:
        respostaPresenca = "Aprovado"

    for chave, valor in conceitos.items():
        
        if nota <= valor:
            respostaNota = chave
    
    return print(f"Então, você está {respostaPresenca} com o conceito {respostaNota}.\n")

# Saída

print(f"\nSua nota é {notaDigitada} e a presença é de {presencaDigitada}%.")
aprovacao(notaDigitada, presencaDigitada)