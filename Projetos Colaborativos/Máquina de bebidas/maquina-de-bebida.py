import json

# Funções de manipulação de JSON
def carregar_json(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_json(arquivo, dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# Exibir produtos
def mostrar_produtos(produtos):
    print("\nProdutos disponíveis:")
    for p in produtos:
        print(f"{p['ID']}. {p['Bebida']} - R${p['Preço'].replace('.', ',')} (Estoque: {p['Estoque']})")

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
        except:
            print("Digite um número válido.")

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
        except:
            print("Digite um valor válido.")

    troco = round(pago - valor, 2)
    if troco > 0:
        print(f"Troco: R${str(troco).replace('.', ',')}")
        distribuir_troco(troco, cedulas, moedas)
    else:
        print("Pagamento exato. Sem troco.")
    return cedulas, moedas

# Distribuição de troco sem sort
def distribuir_troco(troco, cedulas, moedas):
    distribuido = []
    todos = cedulas + moedas
    for i in range(len(todos)):
        todos[i]["Valor"] = float(todos[i]["Valor"])
        todos[i]["Estoque"] = int(todos[i]["Estoque"])

    # Ordenar manualmente (descendente)
    for i in range(len(todos)):
        for j in range(i + 1, len(todos)):
            if todos[i]["Valor"] < todos[j]["Valor"]:
                todos[i], todos[j] = todos[j], todos[i]

    for item in todos:
        valor, estoque = item["Valor"], item["Estoque"]
        count = 0
        while troco >= valor and estoque > 0:
            troco = round(troco - valor, 2)
            estoque -= 1
            count += 1
        item["Estoque"] = estoque
        if count > 0:
            distribuido.append((valor, count))

    if troco > 0:
        print("Troco incompleto por falta de cédulas/moedas.")
    else:
        print("Troco fornecido:")
        for v, q in distribuido:
            print(f"{q}x R${str(v).replace('.', ',')}")

# Modo administrador
def modo_admin(produtos, cedulas, moedas):
    while True:
        print("\n--- MODO ADMINISTRADOR ---")
        print("1. Editar produtos")
        print("2. Editar cédulas")
        print("3. Editar moedas")
        print("4. Sair")
        op = input("Escolha: ")

        if op == "1":
            editar_estoque(produtos, "produto")
        elif op == "2":
            editar_estoque(cedulas, "cédula")
        elif op == "3":
            editar_estoque(moedas, "moeda")
        elif op == "4":
            break
        else:
            print("Opção inválida.")

# Edição de estoque
def editar_estoque(lista, tipo):
    print(f"\nEstoque de {tipo}s:")
    for item in lista:
        nome = item.get("Bebida") or f"R${item['Valor']}"
        print(f"{item['ID']}. {nome} (Estoque: {item['Estoque']})")
    id_editar = input("ID para editar: ")

    for item in lista:
        if item["ID"] == id_editar:
            try:
                novo = int(input("Novo estoque: "))
                item["Estoque"] = str(novo)
                print("Atualizado com sucesso.")
                return
            except:
                print("Entrada inválida.")
                return
    print("ID não encontrado.")

# --- Execução principal ---
produtos = carregar_json("./Projetos Colaborativos/Máquina de bebidas/")
cedulas = carregar_json("./Projetos Colaborativos/Máquina de bebidas/cedulas.json")
moedas = carregar_json("./Projetos Colaborativos/Máquina de bebidas/moedas.json")

print("=== MÁQUINA DE BEBIDAS ===")

while True:
    modo = input("\nDigite 'admin' para modo administrador ou Enter para comprar: ").lower()
    if modo == "admin":
        modo_admin(produtos, cedulas, moedas)
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
