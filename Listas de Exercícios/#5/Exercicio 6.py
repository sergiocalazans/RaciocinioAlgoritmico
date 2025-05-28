# Exercício 6

'''
6.	A distância rodoviária entre algumas capitais brasileiras está disponível na tabela abaixo. 
Para consultar a distância basta cruzar as cidades origem e destino, 
ou seja, a distância entre Curitiba e São Paulo é de 408 km.

Construa um programa que inicialize uma matriz contendo as distâncias apresentadas na tabela acima e 
que então informe ao usuário o tempo necessário para percorrer duas cidades por ele fornecidas.
'''

# Lista de cidades
cidades = ["Curitiba", "Florianópolis", "Porto Alegre", "São Paulo", "Rio de Janeiro"]

# Matriz de distâncias em quilômetros
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

def calcular_tempo(distancia, velocidade=80):
    return distancia / velocidade

print("Cidades disponíveis:", ", ".join(cidades))
origem = input("Informe a cidade de origem: ").strip().title()
destino = input("Informe a cidade de destino: ").strip().title()

i = obter_indice(origem)
j = obter_indice(destino)

if i == -1 or j == -1:
    print("Cidade inválida! Verifique a grafia e tente novamente.")
elif i == j:
    print("A origem e o destino são iguais. Tempo de viagem: 0 horas.")
else:
    distancia = distancias[i][j]
    tempo = calcular_tempo(distancia)
    print(f"\nDistância entre {origem} e {destino}: {distancia} km")
    print(f"Tempo estimado de viagem a 80 km/h: {tempo:.2f} horas")
