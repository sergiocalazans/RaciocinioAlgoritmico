import json
from tabulate import tabulate

# Funções de manipulação de JSON
def carregar_json(arquivo):
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo}' não encontrado.")
        return [] # retorna uma lista vazia para evitar erros posteriores
    except json.JSONDecodeError:
        print(f"Erro: Arquivo '{arquivo}' não é um JSON válido.")
        return []


def salvar_json(arquivo, dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# Exibir produtos usando tabulate
def mostrar_produtos(produtos):
    print("\nProdutos disponíveis:")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    headers = ["ID", "Bebida", "Preço", "Estoque"]
    data = [[p['ID'], p['Bebida'], f"R${p['Preço'].replace('.', ',')}", p['Estoque']] for p in produtos]
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

def mostrar_lista(lista, tipo):
    print(f"\n{tipo.capitalize()}s disponíveis:")
    if not lista:
        print("Nenhum item cadastrado.")
        return
    headers = ["ID", "Item", "Estoque"]
    data = [[item['ID'], item.get("Bebida") or f"R${item['Valor']}", item['Estoque']] for item in lista]
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))


# Escolher produto
def escolher_produto(produtos):
    while True:
        escolha = input("Digite o ID do produto: ")
        for p in produtos:
            if p["ID"] == escolha:
                return p
        print("ID inválido.")

# Solicitar quantidade válida
def solicitar_quantidade(produto):
    estoque = int(produto["Estoque"])
    while True:
        try:
            qtd = int(input("Quantidade desejada: "))
            if 0 < qtd <= estoque:
                return qtd
            print("Quantidade fora do estoque.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

# Calcular valor total
def calcular_pagamento(preco, qtd):
    return round(float(preco) * qtd, 2)

# Pagamento e troco
def pagamento(valor, cedulas, moedas):
    print(f"Total: R${str(valor).replace('.', ',')}")
    while True:
        try:
            pago = float(input("Valor pago: "))
            if pago < valor:
                print("Valor insuficiente.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número.")

    troco = round(pago - valor, 2)
    if troco > 0:
        print(f"Troco: R${str(troco).replace('.', ',')}")
        cedulas, moedas, distribuido = distribuir_troco(troco, cedulas, moedas)
        # Mostrar troco com tabulate
        if distribuido:
            headers = ["Valor", "Quantidade"]
            data = [[f"R${str(v).replace('.', ',')}", q] for v, q in distribuido]
            print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
        else:
            print("Troco incompleto por falta de cédulas/moedas.")
    else:
        print("Pagamento exato. Sem troco.")
    return cedulas, moedas

# Distribuição de troco com sort
def distribuir_troco(troco, cedulas, moedas):
    distribuido = []
    todos = sorted(cedulas + moedas, key=lambda x: float(x["Valor"]), reverse=True)

    for item in todos:
        valor = float(item["Valor"])
        estoque = int(item["Estoque"])
        count = 0
        while troco >= valor and estoque > 0:
            troco -= valor
            estoque -= 1
            count += 1
        item["Estoque"] = estoque
        if count > 0:
            distribuido.append((valor, count))

    return cedulas, moedas, distribuido


# Modo administrador
def modo_admin(produtos, cedulas, moedas):
    senha = input("Digite a senha de administrador: ")
    if senha != "admin":  # Substitua "admin" pela senha desejada
        print("Senha incorreta. Acesso negado.")
        return False

    while True:
        print("\n--- MODO ADMINISTRADOR ---")
        print("1. Ver Produtos")
        print("2. Ver Cédula")
        print("3. Ver Moedas")
        print("4. Editar produtos")
        print("5. Editar cédulas")
        print("6. Editar moedas")
        print("7. Sair")
        op = input("Escolha: ")

        if op == "1":
            mostrar_lista(produtos, "produto")
        elif op == "2":
            mostrar_lista(cedulas, "cédula")
        elif op == "3":
            mostrar_lista(moedas, "moeda")
        elif op == "4":
            editar_produtos(produtos)
        elif op == "5":
            editar_estoque(cedulas, "cédula")
        elif op == "6":
            editar_estoque(moedas, "moeda")
        elif op == "7":
            print("Programa encerrado.")
            return True
        else:
            print("Opção inválida.")

def editar_produtos(produtos):
    while True:
        print("\n--- EDITAR PRODUTOS ---")
        print("1. Criar novo produto")
        print("2. Editar produto existente")
        print("3. Voltar")
        op = input("Escolha: ")

        if op == "1":
            novo_produto = criar_novo_produto()
            if novo_produto:
                produtos.append(novo_produto)
                salvar_json("./Projetos Colaborativos/Máquina de bebidas/produtos.json", produtos)
        elif op == "2":
            editar_estoque(produtos, "produto")
        elif op == "3":
            break
        else:
            print("Opção inválida.")


def criar_novo_produto():
    try:
        id_novo = input("Digite o ID do novo produto: ")
        bebida_novo = input("Digite o nome da bebida: ")
        preco_novo = float(input("Digite o preço da bebida (ex: 5.50): "))
        estoque_novo = int(input("Digite a quantidade em estoque: "))

        return {"ID": id_novo, "Bebida": bebida_novo, "Preço": str(preco_novo), "Estoque": str(estoque_novo)}
    except ValueError:
        print("Erro ao criar produto. Certifique-se de inserir valores numéricos válidos para preço e estoque.")
        return None


# Edição de estoque
def editar_estoque(lista, tipo):
    mostrar_lista(lista, tipo)
    id_editar = input("ID para editar: ")

    for item in lista:
        if item["ID"] == id_editar:
            try:
                novo_estoque = int(input("Novo estoque: "))
                item["Estoque"] = str(novo_estoque)
                print("Atualizado com sucesso.")
                salvar_json(f"./Projetos Colaborativos/Máquina de bebidas/{tipo}s.json", lista)
                return
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")
                return
    print("ID não encontrado.")


# --- Execução principal ---
produtos = carregar_json("./Projetos Colaborativos/Máquina de bebidas/produtos.json")
cedulas = carregar_json("./Projetos Colaborativos/Máquina de bebidas/cedulas.json")
moedas = carregar_json("./Projetos Colaborativos/Máquina de bebidas/moedas.json")

print("=== MÁQUINA DE BEBIDAS ===")

while True:
    modo = input("\nDigite 'admin' para modo administrador ou Enter para comprar: ").lower()
    if modo == "admin":
        if modo_admin(produtos, cedulas, moedas):
            break
        continue

    if not produtos: # Verifica se há produtos para exibir antes de continuar
        print("Não há produtos cadastrados para venda.")
        continue


    mostrar_produtos(produtos)
    produto = escolher_produto(produtos)
    qtd = solicitar_quantidade(produto)
    total = calcular_pagamento(produto["Preço"], qtd)
    produto["Estoque"] = str(int(produto["Estoque"]) - qtd)

    cedulas, moedas = pagamento(total, cedulas, moedas)

    salvar_json("./Projetos Colaborativos/Máquina de bebidas/produtos.json", produtos)
    salvar_json("./Projetos Colaborativos/Máquina de bebidas/cedulas.json", cedulas)
    salvar_json("./Projetos Colaborativos/Máquina de bebidas/moedas.json", moedas)

    if input("Deseja fazer nova operação? (s/n): ").lower() != "s":
        print("Programa encerrado.")
        break
