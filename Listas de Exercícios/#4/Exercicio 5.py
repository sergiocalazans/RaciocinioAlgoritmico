# Exercício 5

'''
5.	Ler 4 números inteiros e calcular a soma dos que forem par. 
'''

# Entrada

contador = 1
lista = []
soma = 0

while contador <= 4:

    num = int(input("\nDigite um número inteiro: "))
    lista.append(num)
    contador += 1

# Processamento 

for valor in lista:

    if valor % 2 == 0:

        soma += valor

# Saída 

print(f"\nA soma dos números pares é: {soma}\n")

