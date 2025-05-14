# Exercício 12

'''
12.	Desenvolva um programa que leia um vetor de 20 posições inteiras e o 
coloque em ordem crescente, utilizando a seguinte estratégia de ordenação: 

• selecione o elemento do vetor de 20 posições que apresenta o menor valor; 

• troque este elemento pelo primeiro; 

• repita estas operações, envolvendo agora apenas os 19 elementos restantes 
(trocando o de menor valor com a segunda posição), depois os 18 elementos 
(trocando o de menor valor com a terceira posição), depois os 17, 16 e assim por diante, 
até restar um único elemento, o maior deles. 

Observação: este método de ordenação é conhecido como “Seleção Direta”.

'''

# Entrada

vetor = []
print("\nDigite 20 números inteiros:")
i = 0

while i < 20:
    try:
        num = int(input(f"Número {i + 1}: "))
        vetor.append(num)
        i += 1
    except ValueError:
        print("\nEntrada inválida. Digite um número inteiro.\n")

# Processamento

i = 0
while i < 19: 
    menor_indice = i
    j = i + 1

    while j < 20:
        if vetor[j] < vetor[menor_indice]:
            menor_indice = j
        j += 1
    
    temp = vetor[i]
    vetor[i] = vetor[menor_indice]
    vetor[menor_indice] = temp
    i += 1

# Saída
print(f"\nVetor em ordem crescente:\n{vetor}\n")
