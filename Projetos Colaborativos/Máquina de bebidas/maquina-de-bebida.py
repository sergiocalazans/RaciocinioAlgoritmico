import json
from tabulate import tabulate

# Funções de manipulação de JSON
def carregar_json(arquivo):
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo}' não encontrado.")
        return []
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
        if distribuido:
            headers = ["Valor", "Quantidade"]
            data = [[f"R${str(v).replace('.', ',')}", q] for v, q in distribuido]
            print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
        else:
            print("Troco incompleto por falta de cédulas/moedas.")
    else:
        print("Pagamento exato. Sem troco.")
    return cedulas, moedas

def distribuir_troco(troco, cedulas, moedas):
    distribuido = []
    lista_original = cedulas + moedas
    todos = []

    # Ordenação manual (ordem decrescente por valor)
    usados = [False] * len(lista_original)
    while len(todos) < len(lista_original):
        maior_valor = -1
        indice_maior = -1
        for i, item in enumerate(lista_original):
            if not usados[i]:
                valor_atual = float(item["Valor"])
                if valor_atual > maior_valor:
                    maior_valor = valor_atual
                    indice_maior = i
        usados[indice_maior] = True
        todos.append(lista_original[indice_maior])

    # Distribuição do troco
    for item in todos:
        valor = float(item["Valor"])
        estoque = int(item["Estoque"])
        count = 0
        while troco >= valor and estoque > 0:
            troco = round(troco - valor, 2)
            estoque -= 1
            count += 1
        item["Estoque"] = estoque
        if count > 0:
            distribuido.append((valor, count))

    return cedulas, moedas, distribuido


# Modo administrador
def modo_admin(produtos, cedulas, moedas):
    senha = input("Digite a senha de administrador: ")
    if senha != "usuarioburro":
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

# Criar produto
def criar_novo_produto():
    try:
        id_novo = input("Digite o ID do novo produto: ")
        bebida_novo = input("Digite o nome da bebida: ")
        preco_novo = float(input("Digite o preço da bebida (ex: 5.50): "))
        estoque_novo = int(input("Digite a quantidade em estoque: "))
        return {"ID": id_novo, "Bebida": bebida_novo, "Preço": str(preco_novo), "Estoque": str(estoque_novo)}
    except ValueError:
        print("Erro ao criar produto. Verifique os valores.")
        return None

# Menu principal de edição de produtos
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
            editar_produto_existente(produtos)
        elif op == "3":
            break
        else:
            print("Opção inválida.")

# Subopções de edição de produto existente
def editar_produto_existente(produtos):
    mostrar_produtos(produtos)
    id_editar = input("Digite o ID do produto a ser editado: ")
    produto = next((p for p in produtos if p["ID"] == id_editar), None)

    if not produto:
        print("ID não encontrado.")
        return

    while True:
        print("\n-- O que deseja editar? --")
        print("1. Editar totalmente o produto")
        print("2. Editar nome")
        print("3. Editar preço")
        print("4. Editar estoque")
        print("5. Voltar")
        op = input("Escolha: ")

        if op == "1":
            editar_produto_totalmente(produto)
        elif op == "2":
            editar_nome_produto(produto)
        elif op == "3":
            editar_preco_produto(produto)
        elif op == "4":
            editar_estoque_produto(produto)
        elif op == "5":
            break
        else:
            print("Opção inválida.")

    salvar_json("./Projetos Colaborativos/Máquina de bebidas/produtos.json", produtos)

def editar_produto_totalmente(produto):
    try:
        novo_nome = input(f"Nome atual: {produto['Bebida']}\nNovo nome: ")
        novo_preco = float(input(f"Preço atual: R${produto['Preço']}\nNovo preço: "))
        novo_estoque = int(input(f"Estoque atual: {produto['Estoque']}\nNovo estoque: "))
        produto["Bebida"] = novo_nome
        produto["Preço"] = str(novo_preco)
        produto["Estoque"] = str(novo_estoque)
        print("Produto atualizado com sucesso.")
    except ValueError:
        print("Erro ao editar. Verifique os valores.")

def editar_nome_produto(produto):
    novo_nome = input(f"Nome atual: {produto['Bebida']}\nNovo nome: ")
    produto["Bebida"] = novo_nome
    print("Nome atualizado com sucesso.")

def editar_preco_produto(produto):
    try:
        novo_preco = float(input(f"Preço atual: R${produto['Preço']}\nNovo preço: "))
        produto["Preço"] = str(novo_preco)
        print("Preço atualizado com sucesso.")
    except ValueError:
        print("Valor inválido.")

def editar_estoque_produto(produto):
    try:
        novo_estoque = int(input(f"Estoque atual: {produto['Estoque']}\nNovo estoque: "))
        produto["Estoque"] = str(novo_estoque)
        print("Estoque atualizado com sucesso.")
    except ValueError:
        print("Valor inválido.")

# Edição de estoque para cédulas/moedas
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

caminho = "./Projetos Colaborativos/Máquina de bebidas/"

produtos = carregar_json(caminho,"produtos.json")
cedulas = carregar_json(caminho, "cedulas.json")
moedas = carregar_json(caminho, "moedas.json")

print("=== MÁQUINA DE BEBIDAS ===")

while True:
    modo = input("\nDigite 'admin' para modo administrador ou Enter para comprar: ").lower()
    if modo == "admin":
        if modo_admin(produtos, cedulas, moedas):
            break
        continue

    if not produtos:
        print("Não há produtos cadastrados para venda.")
        continue

    mostrar_produtos(produtos)
    produto = escolher_produto(produtos)
    qtd = solicitar_quantidade(produto)
    total = calcular_pagamento(produto["Preço"], qtd)
    produto["Estoque"] = str(int(produto["Estoque"]) - qtd)

    cedulas, moedas = pagamento(total, cedulas, moedas)

    salvar_json(f"{caminho}produtos.json", produtos)
    salvar_json(f"{caminho}cedulas.json", cedulas)
    salvar_json(f"{caminho}moedas.json", moedas)

    if input("Deseja fazer nova operação? (s/n): ").lower() != "s":
        print("Programa encerrado.")
        break


print("Agradeçemos por utilizar! Desenvolvido por: Isabelle, Libia e Sérgio.")