# Exercício 2

'''
2.	Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos. 
Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, verificar se n é triangular.
'''

# ENTRADA

num = int(input("\nDigite um número inteiro: "))
triangular = 0
verificacao = False

# PROCESSAMENTO

def numero_triangular(numero):

    global verificacao, triangular

    for i in range(1, numero):

        triangular = (i * (i + 1)) // 2

        if triangular == num:
            verificacao = True

    if verificacao:
        print(f"\nO número {numero} é triangular.\n")
    else:
        print(f"\nO número {numero} não é triangular.\n")

# SAÍDA

numero_triangular(num)