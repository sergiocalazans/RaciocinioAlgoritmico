# Exercício 1

'''
1.	Ler do teclado uma quantidade de números inteiros a serem lidos e calcular:
a) a soma total entre eles
b) a soma dos que forem pares. 
c) a soma dos que forem ímpares
d) a amplitude amostral considerando todos os números lidos (diferença entre o maior e o menor)
'''

# ENTRADA

list_num = []

while True:
    num = int(input("\nDigite um número inteiro: "))

    list_num += [num]

    continuar = int(input("Deseja digitar mais um número? (1-sim ou 2-não)"))

    if continuar == 2:
        break

print(f"\n{list_num}")

# PROCESSAMENTO

def calculos(lista):

    soma = sum(lista)
    soma_pares = []
    soma_impares = []

    for item in lista:

        if num % 2 == 0:
            soma_pares += [item]
        else:
            soma_impares += [item]
    
    soma_pares = sum(soma_pares)
    soma_impares = sum(soma_impares) 

    amp_amostral = max(list_num) - min(list_num)

    print(f"\nA soma total dos números é: {soma};")
    print(f"A soma dos pares é {soma_pares} e dos ímpares é {soma_impares};")
    print(f"Por fim, a amplitude amostral dos números é {amp_amostral}.")

# SAÍDA

calculos(list_num)