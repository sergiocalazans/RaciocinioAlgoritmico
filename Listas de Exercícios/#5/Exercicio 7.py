# Exercício 7

'''
7.	Considerando a mesma tabela da questão anterior, 
desenvolva um programa que permita ao usuário informar várias cidades em sequência, 
até inserir um código finalizador. Mostre então as cidades que compõem o roteiro fornecido, 
a distância de cada percurso intermediário e a distância total do roteiro fornecido.
'''

# Lista de cidades e matriz de distâncias
cidades = ["Curitiba", "Florianópolis", "Porto Alegre", "São Paulo", "Rio de Janeiro"]
distancias = [
    [0,   310, 716, 408, 852],
    [310,   0, 470, 705, 1144],
    [716, 470,   0, 1119, 1553],
    [408, 705, 1119,   0, 429],
    [852, 1144, 1553, 429, 0]
]

def obter_indice(cidade):
    try:
        return cidades.index(cidade)
    except ValueError:
        return -1

print("Cidades disponíveis:", ", ".join(cidades))
print("Digite as cidades em ordem do roteiro. Digite 'FIM' para encerrar.\n")

roteiro = []
while True:
    entrada = input("Digite uma cidade: ").strip().title()
    if entrada == "Fim":
        break
    indice = obter_indice(entrada)
    if indice == -1:
        print("Cidade inválida. Tente novamente.")
    else:
        roteiro.append(indice)

if len(roteiro) < 2:
    print("\nRoteiro insuficiente. É necessário pelo menos duas cidades.")
else:
    print("\nRoteiro informado:")
    total = 0
    for i in range(len(roteiro) - 1):
        origem = cidades[roteiro[i]]
        destino = cidades[roteiro[i+1]]
        dist = distancias[roteiro[i]][roteiro[i+1]]
        print(f"De {origem} até {destino}: {dist} km")
        total += dist
    print(f"\nDistância total do roteiro: {total} km")
