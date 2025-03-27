# Exercício 1

'''
1.	Imprima os números de 1 até 99, com incremento de 2. 

Exemplo: 1, 3, 5.....97, 99
'''

# Entrada

contador = 1
listaNum = [contador]

# Processamento

while contador <= 99:

    if contador == 99:
        break
    
    contador += 2
    listaNum += [contador]

# Saída

print(f"\n{listaNum}\n")

