# Exercício 1

''' 
Dado o exercício do cálculo da média, verificar se o aluno está
aprovado.
'''

# Definindo as variáveis de Entrada

primeiraNota = float(input("Digite a sua primeira nota: "))
segundaNota = float(input("Digite a sua segunda nota: "))
terceiraNota = float(input("Digite a sua terceira nota: "))

listaNotas = [primeiraNota, segundaNota, terceiraNota]

# Processamento

mediaNotas = sum(listaNotas) / len(listaNotas)

def aprovacao(media):

    resposta = ""

    if media < 4:
        resposta = "Reprovado"
    elif media < 7:
        resposta = "Recuperação"
    else:
        resposta = "Aprovado"
    
    return print(f"A média de suas notas é: {round(media, 2)} e o resultado é {resposta}")

# Saída

aprovacao(mediaNotas)
