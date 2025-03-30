# Exercício 10

'''
10.	Uma empresa de câmbio permite a compra de dólares, libras e euros. 
Elabore um algoritmo que leia o código da moeda que o cliente quer comprar e 
qual o montante que ele quer adquirir nessa moeda. 
Mostre então quanto ele deverá pagar em reais para concretizar a operação. 
Além da cotação, a empresa cobra uma comissão de 5% (quando o valor for menor que R$ 1.000), 
ou de 3% (quando maior ou igual a R$1.000). Considere o câmbio do dia. 

'''

# Entrada

moeda = input("\nInforme a moeda (USD, EUR, GBP): ").strip().upper()
quantidade = float(input("Informe a quantidade desejada: "))

# Processamento

def obterCotacao(moeda): 
    cotacoes = {
        'USD': 5.76,  # Cotação para Dólar
        'EUR': 6.23,  # Cotação para Euro
        'GBP': 7.45   # Cotação para Libra
    }
    return cotacoes.get(moeda.upper(), None)

cotacao = obterCotacao(moeda)

def calculoCotacao(cot): # cot - cotação

    if cot:
        valorReais = quantidade * cotacao

        if valorReais < 1000:
            comissao = valorReais * 0.05
        else:
            comissao = valorReais * 0.03

        total = valorReais + comissao

        print(f"\nCotação do {moeda}: R$ {cotacao:.2f}")
        print(f"Valor sem comissão: R$ {valorReais:.2f}")
        print(f"Comissão: R$ {comissao:.2f}")
        print(f"Total a pagar: R$ {total:.2f}\n")

    else:
        print("\nMoeda inválida. Escolha entre USD, EUR ou GBP.\n")

# Saída

calculoCotacao(cotacao)