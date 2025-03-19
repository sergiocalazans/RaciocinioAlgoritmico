# Resolução Exercício 4

''' 4. Faça um algoritmo que recebe o valor de um produto e calcule os seguintes valores: 
(1) a vista com 5% de desconto; (2) o valor da parcela em 2x; (3) o valor da parcela em 3x com acréscimo de 5%.'''

# Definindo as variáveis de Entrada

valorProduto = float(input("Digite o valor do produto: (Formato: xxx.xx) "))
desconto = 0.05

# Processamento

valorDescontoProduto = valorProduto * desconto
valorProduto3x = f"R$ {((valorProduto + valorDescontoProduto) / 3):_.2f}".replace('.',',').replace('_','.')
valorProduto2x = f"R$ {(valorProduto / 2):_.2f}".replace('.',',').replace('_','.')
valorProduto1x = f"R$ {(valorProduto - valorDescontoProduto):_.2f}".replace('.',',').replace('_','.')

# Saída

print(" \n O produto tem os seguintes valores: \n")
print(f" - À Vista: {valorProduto1x} \n - Parcela em 2x: {valorProduto2x} \n - Parcela em 3x (com acréscimo de {desconto * 100}%): {valorProduto3x} \n")