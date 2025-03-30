# Exercício 3

'''
3.	Imprima os números de -100 até 100, com incremento de 10. 
Exemplo: -100, -90, -80.....90, 100
'''

# Entrada 

contador = -100
listaNum = [contador]

# Processamento

while contador <= 100:

    if contador == 100:
        break
    
    contador += 10
    listaNum += [contador]

# Saída

print(f"\n{listaNum}\n")