# Exercício 9

'''
9.	Imprima os números múltiplos de 3 entre li (limite inicial) e lf (limite final). 
Os valores inteiros de li e lf devem ser informados pelo usuário e não pertencem ao intervalo, ou seja, intervalo aberto.

'''

# Entrada

li = int(input("\nInforme o limite inicial (li): "))
lf = int(input("Informe o limite final (lf): "))
listaNum = []

# Processamento

for num in range(li + 1, lf):  # Intervalo aberto (li, lf)
    if num % 3 == 0:
        listaNum += [num]

# Saída

print(f"\nMúltiplos de 3 no intervalo aberto ({li}, {lf}):\n\n{listaNum}\n")