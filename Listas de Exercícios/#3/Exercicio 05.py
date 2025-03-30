# Exercício 5

'''
5.	Imprima os números ímpares de 1 até n, sendo n fornecido pelo usuário.
'''

# Entrada 

intervaloMax = int(input("Digite o número máximo do intervalo: "))
contador = 1
listaNum = []

# Processamento

while contador <= intervaloMax:

    if contador % 2 != 0:
        listaNum += [contador]
    
    contador += 1

# Saída

print(f"\nNo intervalo de 1 até {intervaloMax}, esses são os números ímpares:\n \n{listaNum}\n")