# Importando a biblioteca Datetime
import datetime

# Definindo as variáveis de Entrada
anoAtual = datetime.date.today().year
cadastro = {}

# Processamento
while True:
    
    nome = str(input("Nome:")).strip()
    anoNascimento = int(input("Ano de Nascimento:"))

    idade = anoAtual - anoNascimento

    cadastro[nome] = (anoNascimento, idade)

    continuar = str(input("Há mais pessoas para cadastrar? (sim/não): ")).strip().lower()

    if continuar != "sim":
        break

# Saída
print(f"{'Nome':<10} {'Ano de Nascimento':<20} {'Idade':<6}")
print("-" * 40)

for nome, dados in cadastro.items():
    anoNascimento, idade = dados  
    print(f"{nome:<10} {anoNascimento:<20} {idade:<6}")

 