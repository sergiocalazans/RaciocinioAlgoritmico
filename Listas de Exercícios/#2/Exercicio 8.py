# Exercício 8

'''
8.	Em um determinado estacionamento a primeira hora custa R$ 8,00, que é o valor mínimo praticado. 
Após uma hora o valor é fracionado, R$ 1,50 a cada 15 minutos. 
Elabore um algoritmo que leia um número inteiro correspondente a quantidade de minutos usados no estacionamento 
e mostre a mensagem “Valor mínimo, R$ 8,00” ou “Valor fracionado, R$ x”, 
no qual x será o valor a pagar calculado pelo algoritmo.
'''

# Entrada

minutos = int(input("\nDigite a quantidade de minutos usados no estacionamento: "))

# Processamento

def calcularValorEstacionamento(min):
    valorMinimo = 8.00
    fracao15min = 1.50
    
    if min <= 60:
        return print(f"\nValor mínimo, R$ {valorMinimo:.2f}.\n")
    else:
        # Calcula minutos excedentes além da primeira hora
        minutosExcedentes = min - 60
        
        # Calcula quantas frações de 15 minutos existem nos minutos excedentes
        fracoes = (minutosExcedentes + 14) // 15  # Arredondamento para cima
        
        # Calcula o valor total
        valorTotal = valorMinimo + (fracoes * fracao15min)
        
        return print(f"\nValor fracionado, R$ {valorTotal:.2f}.\n")

# Exemplo de uso

calcularValorEstacionamento(minutos)
