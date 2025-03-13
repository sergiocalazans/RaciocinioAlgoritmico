# Resolução Exercício 3

# Definindo as variáveis de Entrada 

salarioMinimo = 1518
salarioDigitado = int(input("Digite o seu salário profissional:"))

# Processamento

calculoSalarioMinimo = float(salarioDigitado / salarioMinimo)

# Saída

print(f"Você recebe {round(calculoSalarioMinimo, 2)} salários mínimo.")