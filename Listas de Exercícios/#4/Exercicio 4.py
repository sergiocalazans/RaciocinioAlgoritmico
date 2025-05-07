# Exercício 4

'''
4.	Leia dois valores reais do teclado, calcular e imprimir na tela: 

a)	A soma destes valores 
b) O produto deles 
c) O quociente entre eles

'''

# Entrada

contador = 1
lista = []

while contador <= 2:

    num = float(input("\nDigite um número: "))
    lista.append(num)
    contador += 1

# Processamento e Saída

print(f"\na) Soma: {sum(lista)}")
print(f"\nb) Produto: {round((lista[0] * lista[1]), 2)}")
print(f"\nc) Quociente: {round((lista[0] / lista[1]), 2)}\n")