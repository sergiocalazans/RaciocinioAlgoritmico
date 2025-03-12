# Importando a biblioteca Datetime

import datetime

# Definindo as variáveis de Entrada

anoAtual = datetime.date.today().year
cadastro = {}

# Processamento

while True:
    
    nome = str(input("Qual o seu nome?")).strip()
    anoNascimento = int(input("Qual foi o ano que você nasceu?")).strip()

    idade = anoAtual - anoNascimento

    cadastro[nome] = anoNascimento

    continuar = str(input("Há mais pessoas para cadastrar? (sim/não): ")).strip().lower()

    if continuar != "sim":
        break

# Saída

for chave in cadastro.keys():
    print(chave)
 