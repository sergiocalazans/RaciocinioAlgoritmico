# Exercício 6

'''
6.	Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos. 
Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, verificar se n é triangular.
'''

# Entrada
num = int(input("\nDigite um número inteiro: "))
x = 1
triangular = [0] # Números triangulares

# Processamento e Saída

while triangular[-1] <= num:

    triangular.append((x * (x + 1)) // 2)
    x += 1
    
    if num in triangular:
        print(f"\nO número {num} é triangular")
        break


if num not in triangular:
    print(f"\nO número {num} não é triangular")

triangular.pop(0)
print(triangular)
    
