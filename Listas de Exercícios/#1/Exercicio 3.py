# Resolução Exercício 3

''' 3. Faça um algoritmo que receba o salário de um profissional e calcule quantos salário mínimos ele recebe.'''

# Definindo as variáveis de Entrada 

salarioMinimo = 1518
salarioDigitado = float(input("Digite o seu salário profissional: (formato: xxxx.xx)"))

# Processamento

calculoSalarioMinimo = float(salarioDigitado / salarioMinimo)

# Saída

print(f"Você recebe {round(calculoSalarioMinimo, 2)} salários mínimo.")