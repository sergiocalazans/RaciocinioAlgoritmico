# Exercício 3

'''
3.	Leia três números do teclado e verificar se o primeiro é maior que a soma dos outros dois.
'''

# Entrada

contador = 1
lista = []

while contador <= 3:

    num = int(input("\nDigite um número inteiro: "))
    lista.append(num)
    contador += 1

# Processamento e Saída

if lista[0] > sum(lista[-2:]):

    print("\nO primeiro número digitado, é maior do que a soma dos últimos números.\n")

else:

    print("\nO primeiro número digitado, não é maior do que a soma dos últimos números.\n")