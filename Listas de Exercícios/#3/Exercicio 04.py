# Exercício 4

'''
4.	Imprima os números múltiplos de 4 existentes no intervalo aberto de 1 a 100.
'''

# Entrada
contador = 1
listaNum = []

# Processamento

while contador <= 100:

    if contador % 4 == 0:
        listaNum += [contador]
    
    contador += 1

# Saída

print(f"\n{listaNum}\n")