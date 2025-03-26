# Exercício 5

'''
5.	Em uma determinada papelaria a fotocópia custa R$ 0,25, caso sejam tiradas menos de 100 cópias. 
A partir de 100 cópias, o valor de cada fotocópia tirada cai para R$ 0,20. 
Elabore um algoritmo que leia o número de cópias e mostre o valor a pagar pelo serviço.
'''

# Entrada

numFotocopia = round(int(input("\nDigite a quantidade de fotocópias: ")), 2)

# Processamento

def calculoFotocopias(qtd):

    if qtd < 100:
        qtdPreco = f"R$ {qtd * 0.25}"
    else:
        qtdPreco = f"R$ {qtd * 0.20}"

    return print(f"\nO valor é de {qtdPreco.replace('.', ',')}.\n")

# Saída

calculoFotocopias(numFotocopia)