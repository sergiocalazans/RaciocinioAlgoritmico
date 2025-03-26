# Exercício 13

'''
13. Em uma determinada loja de eletrodomésticos, os produtos podem ser adquiridos da seguinte forma: 

Opção     Condição          Cálculo

1         à vista           8% de desconto
2         em 2 parcelas     4% de desconto, dividido em duas vezes
3         em 3 parcelas     sem desconto, dividido em três vezes
4         em 4 parcelas     4% de acréscimo, dividido em quatri vezes

Elabore um algoritmo que leia a opção do cliente e o preço de tabela do produto, 
mostrando então o valor calculado conforme a condição escolhida. 

'''

# Entrada

precoProduto = float(input("\nDigite o preço do produto: "))

while True:
    opcao = int(input("\nEscolha a opção de pagamento (1, 2, 3 ou 4): "))
    
    if opcao in [1, 2, 3, 4]:  
        print("Opção válida.")
        break
    else:
        print("Opção inválida. Tente novamente.")
    

# Processamento

def calcularPagamento(op, pp): # op - opção e pp - preço produto

    if op == 1:
        valorFinal = pp * 0.92  # 8% de desconto
        return f"Valor final à vista: R$ {valorFinal:.2f}"
    
    elif op == 2:
        valorFinal = pp * 0.96  # 4% de desconto
        parcela = valorFinal / 2
        return f"Valor final em 2x: R$ {valorFinal:.2f} (2x de R$ {parcela:.2f})"
    
    elif op == 3:
        parcela = pp / 3
        return f"Valor final em 3x: R$ {pp:.2f} (3x de R$ {parcela:.2f})"
    
    elif op == 4:
        valorFinal = pp * 1.04  # 4% de acréscimo
        parcela = valorFinal / 4
        return f"Valor final em 4x: R$ {valorFinal:.2f} (4x de R$ {parcela:.2f})"
    
    else:
        return "Valor não encontrado"

# Exemplo de uso

print(f"\n{calcularPagamento(opcao, precoProduto)}.\n")
