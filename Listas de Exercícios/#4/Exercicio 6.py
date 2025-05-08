# Exercício 6

'''
6.	Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos. 
Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, verificar se n é triangular.
'''

# Entrada
num = int(input("\nDigite um número inteiro: "))
i = [] #
x = 1
triangular = [] # Números triangulares

# Processamento e Saída

while i <= num:

    triangular.append((x * (x + 1)) // 2)
    x += 1
    i.append(triangular[-1])
    
    if num in triangular:
        print("\né triangular")
        break


if num not in triangular:
    print("\nnão é triangular")

print(triangular)
    
