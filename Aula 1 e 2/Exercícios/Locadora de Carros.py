# Exercicio 2

# Definindo as variáveis de Entrada

print("Bem-vindo à Locadora Carros Curitiba!")

valorLocacao = 100.00
diasLocacao = int(input("Por quantos dias, você vai ficar com o carro?"))

# Processamento

calculoLocacao = round(valorLocacao * diasLocacao, 2)

# Saída

calculoLocacao = str(calculoLocacao).replace('.', ',').replace('_', '.')
resultado = print(f"O valor é: R$ {calculoLocacao}")