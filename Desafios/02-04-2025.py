x = int(input('Entrada ')) # qtd de interações

cont = 0
w = 0

# Laço de repetição para verificar a soma de um intervalo de números
while cont < x:

    y = int(input('Entrada ')) # Valor de Entrada
    w = 1
    a = 0 # Soma 

    while w <= y: # Laço de repetição de 1 até o valor de entrada

        a += w
        w += 1
    
    print(y, a)
    cont += 1