# Exercício 2

'''
2.	Imprima os números de 50 até 0 com decremento de 5. 

Exemplo: 50, 45, 40.....5, 0
'''

# Entrada

contador = 50
listaNum = [contador]

# Processamento

while contador >= 5:

    if contador == 5:
        break
    
    contador -= 5
    listaNum += [contador]

# Saída

print(f"\n{listaNum}\n")