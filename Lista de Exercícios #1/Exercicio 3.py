# Resolução Exercício 3

# Definindo as variáveis de Entrada 

salarioMinimo = 1518
salarioDigitado = int(input("Digite o seu salário profissional:"))

# Processamento

calculoSalarioMinimo = float(salarioDigitado / salarioMinimo)

# Saída

print(f"Você recebe {calculoSalarioMinimo:,.2f} salários mínimo.")