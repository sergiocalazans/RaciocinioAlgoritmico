# Resolução Exercício 6

'''
6. Faça um algoritmo que calcule a quantidade de latas de tintas necessárias para pintar um tanque cilindro, 
em que são fornecidas sua altura e raio, sabendo que:

    a.	A lata de tinta custa R$ 50,00;
    b.	Cada lata contém 5 litros;
    c.	Cada litro de tinta pinta 3 metros quadrados;
    d.	Entrada do programa: altura e raio do cilindro;
    e.	Saída: valor em reais e quantidade de latas.
'''


# Importando a biblioteca Math
import math

# Definição de Entradas
alturaCilindro = float(input("Qual à altura do cilindro? (em metros, formato: xx.xx) "))
raioCilindro = float(input("Qual o raio do cilindro? (em metros, formato: xx.xx) "))

# Definição de constantes
valorTinta = 50  # Valor por lata
litrosPorLata = 5  # Cada lata contém 5 litros
coberturaPorLitro = 3  # Cada litro pinta 3 m²

# Cálculo da área total do cilindro
areaCilindro = 2 * math.pi * raioCilindro * (raioCilindro + alturaCilindro)

# Quantidade de litros de tinta necessária
litrosNecessarios = areaCilindro / coberturaPorLitro

# Quantidade de latas necessárias (sempre arredondando para cima)
qtdLatas = math.ceil(litrosNecessarios / litrosPorLata)

# Valor total
valorFinal = round(qtdLatas * valorTinta, 2)

# Saída formatada
print(f"\nA área do cilindro é de: {round(areaCilindro, 2)} m². \n")
print(f"Serão necessárias {qtdLatas} lata(s) de tinta(s). \n")
print(f"Custo total: R$ {valorFinal:.2f}".replace('.', ','))

