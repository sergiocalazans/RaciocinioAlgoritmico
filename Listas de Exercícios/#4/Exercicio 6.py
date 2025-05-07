# Exercício 6

'''
6.	Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos. 
Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, verificar se n é triangular.
'''

# Entrada
num = int(input("\nDigite um número inteiro: "))
i = 1 # Contador
triangular = [] # Números traingulares

# Processamento e Saída

while True:

    triangular.append((i * (i + 1)) // 2)
    i += 1

    if num in triangular:
        print("\né triangular")
        break
    
    elif num > triangular[-1]:
        print("\nnão é triangular")
        break

print(triangular)
    
