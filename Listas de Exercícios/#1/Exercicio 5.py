# Resolução Exercício 5

''' 5. Faça um algoritmo que calcule o consumo médio de um automóvel (medido em km/l), 
solicitando como entrada a distância total percorrida (KM) e o 
volume de combustível consumido para percorre-la (litros). '''

# Definindo as variáveis de Entrada

distanciaPercorrida = float(input("Qual foi a distância percorrida? (em Km, formato: xx.xx) "))
volumeConsumido = float(input("Qual foi o volume consumido? (em Litros, formato: xx.xx) "))

# Processamento

consumoMédio = round(distanciaPercorrida / volumeConsumido, 2)

# Saída 

print(f"O consumo médio de combustível do automóvel foi de {consumoMédio} KM/L.")