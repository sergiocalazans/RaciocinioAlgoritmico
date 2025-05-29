from tabulate import tabulate

produtos = [
    ["ID", "Bebida", "Preço", "Estoque"],
    [1, "Coca-cola", 3.75, 2],
    [2, "Pepsi", 3.67, 5],
    [3, "Monster", 9.96, 1],
    [4, "Café", 1.25, 100],
    [5, "Redbull", 13.99, 2]
]

def obter_produto(matriz, indice):
    return matriz[indice]

def selecionar_qtd(vetor):

    produto = str(vetor[1])
    valor = float(vetor[2])
    estoque = int(vetor[3])

    if estoque == 0:
        print("\nEstoque do produto não disponível.")
    else:
        print(f"\nO produto {produto} custa R${valor} com estoque de {estoque}.")

    while True:

        try:
            qtd = int(input(f"Digite a quantidade de bebidas: "))
            if qtd < 0 or qtd > estoque:
                raise ValueError
            else:
                break
        except ValueError:
            print("\nDigite uma quantidade dentro do estoque.")
    
    return produto, valor, qtd
        
def pagar(produto, valor, qtd):

    calculo = valor * qtd
    valor = round(calculo, 2)

    print(f"\nO valor do pagamento da(s) bebida(s) do produto {produto} é: R${valor}")
    return valor

def pagamento(valor):

    while True:
        try:
            qtd_valor = float(input("\nDigite um valor para pagar: "))

            if qtd_valor < valor:
                raise ValueError
            else:
                if qtd_valor > valor:
                    restante = float(qtd_valor - valor)
                else:
                    restante = float(0)
                break
        except ValueError:
            print("\nDigite um valor suficiente para pagar.")
    
    return restante

# Função para verificar se continua o programa
def verificador(valor):

    while valor not in [1, 2]: # enquanto o valor colocado pelo usuário for diferente dos ultilizados na execução

        print("\nValor Inválido!")
        valor = input("\nVocê quer comprar mais? (1-sim ou 2-não) ") 

    if valor == 1:
        return False # se for falso, o loop quebrará e encerrará o programa
    elif valor == 2:
        return True

print(tabulate(produtos, headers="firstrow", tablefmt="fancy_grid"))

while True:

    escolha = int(input("\nEscolha um produto, digitando o seu ID (identificador): "))
    escolha = obter_produto(produtos, escolha)
    bebida, valor_final, quantidade = selecionar_qtd(escolha)
    valor_final = pagar(bebida, valor_final, quantidade)
    troco = pagamento(valor_final)
    print(f"\nCompra finalizada!\nVocê comprou {quantidade} bebida(s) do produto {bebida}.\nO valor final foi de R${valor_final} e o troco é R${troco}\n")
    continuar = int(input("\nVocê quer comprar mais? (1-sim ou 2-não) "))
    continuar = verificador(continuar)

    if not continuar:
        print("\nPrograma encerrado.")
        break
    