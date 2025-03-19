# Exercício 1

# Definindo as variáveis de Entrada

primeiraNota = float(input("Digite a sua primeira nota: "))
segundaNota = float(input("Digite a sua segunda nota: "))
terceiraNota = float(input("Digite a sua terceira nota: "))

listaNotas = [primeiraNota, segundaNota, terceiraNota]

# Processamento

mediaNotas = sum(listaNotas) / len(listaNotas)

# Saída

print(f"A média de suas notas é: {round(mediaNotas, 2)}")
