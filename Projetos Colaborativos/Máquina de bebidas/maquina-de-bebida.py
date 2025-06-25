# Importa a biblioteca json para leitura e escrita de arquivos JSON
import json
# Importa a função tabulate para exibir dados em formato de tabela no terminal
from tabulate import tabulate

# === Função para formatar o valor de dinheiro ===

def formatar(valor):
    """
    Formata um valor numérico para o padrão de moeda brasileiro (R$ X.XXX,XX).
    A função é robusta e lida com valores em formato de string ou número.
    """
    try:
        # Converte o valor para float, pois a formatação f-string requer um número.
        # Isso é crucial, pois os valores lidos do JSON vêm como string.
        valor_numerico = float(valor)
    except (ValueError, TypeError):
        # Caso a conversão falhe (ex: texto não numérico), retorna um valor padrão.
        return "R$ --,--"

    # Formata o número com duas casas decimais e usa '_' como separador de milhar temporário.
    # Exemplo: 1234.50 se torna "1_234.50"
    texto_formatado = f"R${valor_numerico:_.2f}"

    # A ordem das substituições é importante.
    # Primeiro, trocamos o ponto decimal por vírgula.
    # Exemplo: "R$1_234.50" se torna "R$1_234,50"
    texto_formatado = texto_formatado.replace('.', ',')

    # Depois, trocamos o separador de milhar temporário '_' por ponto.
    # Exemplo: "R$1_234,50" se torna "R$1.234,50"
    texto_formatado = texto_formatado.replace('_', '.')

    return texto_formatado

# === Funções de manipulação de JSON ===

# Função para carregar dados de um arquivo JSON
def carregar_json(arquivo):
    try:
        # Abre o arquivo no modo leitura com codificação UTF-8
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)  # Retorna o conteúdo carregado
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo}' não encontrado.")  # Mensagem de erro se o arquivo não existir
        return []  # Retorna lista vazia
    except json.JSONDecodeError:
        print(f"Erro: Arquivo '{arquivo}' não é um JSON válido.")  # Mensagem de erro se o arquivo estiver mal formatado
        return []  # Retorna lista vazia

# Função para salvar dados em um arquivo JSON
def salvar_json(arquivo, dados):
    # Abre o arquivo no modo escrita com codificação UTF-8
    with open(arquivo, "w", encoding="utf-8") as f:
        # Escreve os dados em formato JSON com indentação
        json.dump(dados, f, indent=4, ensure_ascii=False)

# === Exibir produtos usando tabulate ===

# Função para exibir produtos cadastrados
def mostrar_produtos(produtos):
    print("\nProdutos disponíveis:")
    if not produtos:  # Verifica se a lista está vazia
        print("Nenhum produto cadastrado.")
        return
    # Define os cabeçalhos da tabela
    headers = ["ID", "Bebida", "Preço", "Estoque"]
    # Monta a lista de dados com formatação de preço
    data = [[p['ID'], p['Bebida'], f"{formatar(p['Preço'])}", p['Estoque']] for p in produtos]
    # Exibe a tabela formatada
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

# Função para exibir cédulas ou moedas cadastradas
def mostrar_lista(lista, tipo):
    # O método capitalize() pega o primeiro caractere de uma string, deixa como maiusculo e o resto minusculo
    print(f"\n{tipo.capitalize()}s disponíveis:")
    if not lista:  # Verifica se a lista está vazia
        print("Nenhum item cadastrado.")
        return
    # Define os cabeçalhos da tabela
    headers = ["ID", "Item", "Estoque"]
    # Monta a tabela com valores e estoques
    data = [[item['ID'], f"{formatar(item['Valor'])}", item['Estoque']] for item in lista]
    # Exibe a tabela formatada
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

# === Escolher produto ===

# Função para escolher um produto pelo ID
def escolher_produto(produtos):
    while True:
        escolha = input("Digite o ID do produto: ")  # Solicita o ID ao usuário
        for p in produtos:
            if p["ID"] == escolha:  # Se o ID for válido, retorna o produto
                return p
        print("ID inválido.")  # Mensagem de erro se ID não for encontrado

# === Solicitar quantidade válida ===

# Função para solicitar a quantidade desejada do produto
def solicitar_quantidade(produto):
    estoque = int(produto["Estoque"])  # Obtém o estoque do produto
    while True:
        try:
            qtd = int(input("Quantidade desejada: "))  # Solicita a quantidade
            if 0 < qtd <= estoque:  # Verifica se a quantidade está disponível
                return qtd
            print("Quantidade fora do estoque.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

# === Calcular valor total ===

# Função que calcula o valor total da compra
def calcular_pagamento(preco, qtd):
    return round(float(preco) * qtd, 2)  # Multiplica o preço pela quantidade

# === Pagamento e troco ===

# Função que gerencia o pagamento e cálculo de troco
def pagamento(valor, cedulas, moedas):
    print(f"Total: {formatar(valor)}")  # Exibe o valor total
    while True:
        try:
            pago = float(input("Valor pago: "))  # Solicita o valor pago
            if pago < valor:
                print("Valor insuficiente.")  # Se o valor for menor que o necessário
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número.")

    troco = round(pago - valor, 2)  # Calcula o troco
    estoque_valores = cedulas + moedas # Estoque das cedulas e moedas

    # Verifica se o troco a ser dado é maior que o total de dinheiro na máquina
    total_disponivel_maquina = sum(float(item['Valor']) * int(item['Estoque']) for item in estoque_valores)
    total_disponivel_maquina = round(total_disponivel_maquina, 2)

    # Se o troco for maior que o dinheiro disponível, cancela a compra e encerra
    if troco > total_disponivel_maquina:

        print("\nDESCULPE! A máquina não possui troco suficiente para esta transação.")
        print(f"Troco necessário: {formatar(troco)}. Disponível na máquina: {formatar(total_disponivel_maquina)}.")
        print(f"Compra cancelada. Devolvendo seu pagamento de {formatar(pago)}.")
        print("Programa encerrado.")
        exit()  # Encerra a execução do programa

    if troco > 0:
        print(f"Troco: {formatar(troco)}")  # Exibe o troco
        cedulas, moedas, distribuido = distribuir_troco(troco, cedulas, moedas)  # Calcula a distribuição do troco
        if distribuido:  # Se houve distribuição possível
            headers = ["Valor", "Quantidade"]
            data = [[f"{formatar(v)}", q] for v, q in distribuido]
            print(tabulate(data, headers=headers, tablefmt="fancy_grid"))  # Exibe a tabela de troco
    else:
        print("Pagamento exato. Sem troco.")
    return cedulas, moedas

# Função para distribuir o troco entre cédulas e moedas
def distribuir_troco(troco, cedulas, moedas):
    distribuido = []  # Lista de itens distribuídos
    lista_original = cedulas + moedas  # Junta cédulas e moedas
    todos = []  # Lista ordenada por valor

    # Ordena manualmente os itens por valor decrescente
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

    # Tenta usar os itens disponíveis para formar o troco
    for item in todos:
        valor = float(item["Valor"])
        estoque = int(item["Estoque"])
        count = 0
        while troco >= valor and estoque > 0:
            troco = round(troco - valor, 2)
            estoque -= 1
            count += 1
        item["Estoque"] = estoque  # Atualiza o estoque
        if count > 0:
            distribuido.append((valor, count))  # Adiciona à lista de troco dado

    return cedulas, moedas, distribuido

# === Modo administrador ===

# Função para entrar no modo administrador
def modo_admin(produtos, cedulas, moedas, caminho):
    senha = input("Digite a senha de administrador: ")
    if senha != "usuario":  # Verifica a senha
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
            mostrar_produtos(produtos)
        elif op == "2":
            mostrar_lista(cedulas, "cédula")
        elif op == "3":
            mostrar_lista(moedas, "moeda")
        elif op == "4":
            editar_produtos(produtos, caminho)
        elif op == "5":
            editar_estoque(cedulas, "cédula", caminho)
        elif op == "6":
            editar_estoque(moedas, "moeda", caminho)
        elif op == "7":
            print("Programa encerrado.")
            return True
        else:
            print("Opção inválida.")

# === Criar produto ===

# Cria e retorna um novo produto com base na entrada do usuário
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

# Permite editar um produto já existente
def editar_produto_existente(produtos, caminho):
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

    salvar_json(f"{caminho}produtos.json", produtos)

# Função que permite criar, editar ou remover produtos
def editar_produtos(produtos, caminho):
    # Início do loop de edição (permite múltiplas ações até o usuário escolher sair)
    while True:
        # Exibe o menu de opções para o administrador
        print("\n--- EDITAR PRODUTOS ---")
        print("1. Criar novo produto")
        print("2. Editar produto existente")
        print("3. Remover produto")  # Opção adicionada
        print("4. Voltar")

        # Solicita a escolha do usuário
        op = input("Escolha: ")

        # Se o usuário escolher criar um novo produto
        if op == "1":
            # Chama a função que coleta dados e retorna um novo produto
            novo_produto = criar_novo_produto()

            # Se o produto foi criado com sucesso (não é None)
            if novo_produto:
                # Adiciona o novo produto à lista
                produtos.append(novo_produto)

                # Salva a lista atualizada no JSON
                salvar_json(f"{caminho}produtos.json", produtos)

        # Se o usuário optar por editar um produto já existente
        elif op == "2":
            editar_produto_existente(produtos, caminho)

        # Se o usuário optar por remover um produto
        elif op == "3":
            remover_produto(produtos, caminho) # Corrigido para passar o caminho

        # Se quiser voltar ao menu anterior
        elif op == "4":
            break  # Sai do loop e retorna

        # Se o usuário digitar uma opção inválida
        else:
            print("Opção inválida.")

# Edita todas as informações do produto
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

# Edita apenas o nome do produto
def editar_nome_produto(produto):
    novo_nome = input(f"Nome atual: {produto['Bebida']}\nNovo nome: ")
    produto["Bebida"] = novo_nome
    print("Nome atualizado com sucesso.")

# Edita apenas o preço do produto
def editar_preco_produto(produto):
    try:
        novo_preco = float(input(f"Preço atual: R${produto['Preço']}\nNovo preço: "))
        produto["Preço"] = str(novo_preco)
        print("Preço atualizado com sucesso.")
    except ValueError:
        print("Valor inválido.")

# Edita apenas o estoque do produto
def editar_estoque_produto(produto):
    try:
        novo_estoque = int(input(f"Estoque atual: {produto['Estoque']}\nNovo estoque: "))
        produto["Estoque"] = str(novo_estoque)
        print("Estoque atualizado com sucesso.")
    except ValueError:
        print("Valor inválido.")

# Função que remove um produto da lista de produtos, apenas se o estoque for 0
def remover_produto(produtos, caminho):
    # Mostra a lista atual de produtos ao administrador
    mostrar_produtos(produtos)

    # Solicita o ID do produto que será removido
    id_remover = input("Digite o ID do produto que deseja remover: ")

    # Procura o produto com base no ID fornecido
    produto = next((p for p in produtos if p["ID"] == id_remover), None)

    # Se o produto não existir, exibe mensagem de erro e sai da função
    if not produto:
        print("Produto não encontrado.")
        return

    # Verifica se o produto ainda tem itens no estoque
    if int(produto["Estoque"]) > 0:
        # Se o estoque for maior que zero, impede a remoção
        print("Erro: só é possível remover produtos com estoque igual a 0.")
        return

    # Solicita confirmação do usuário para remover o produto
    confirmacao = input(f"Tem certeza que deseja remover '{produto['Bebida']}'? (s/n): ").lower()

    # Se o usuário confirmar a remoção
    if confirmacao == "s":
        # Remove o produto da lista
        produtos.remove(produto)

        # Salva a lista atualizada no arquivo JSON
        salvar_json(f"{caminho}produtos.json", produtos)

        # Mensagem de sucesso
        print("Produto removido com sucesso.")
    else:
        # Se o usuário cancelar a ação
        print("Remoção cancelada.")

# === Edição de estoque de cédulas/moedas ===

# Permite alterar o estoque de uma cédula ou moeda
def editar_estoque(lista, tipo, caminho):
    mostrar_lista(lista, tipo)
    id_editar = input("ID para editar: ")

    for item in lista:
        if item["ID"] == id_editar:
            try:
                novo_estoque = int(input("Novo estoque: "))
                item["Estoque"] = str(novo_estoque)
                print("Atualizado com sucesso.")
                salvar_json(f"{caminho}{tipo}s.json", lista)
                return
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")
                return
    print("ID não encontrado.")

# === Execução principal ===

# Define o caminho base para os arquivos JSON
caminho = "./Projetos Colaborativos/Máquina de bebidas/"

# Carrega os dados dos arquivos
produtos = carregar_json(caminho + "produtos.json")
cedulas = carregar_json(caminho + "cedulas.json")
moedas = carregar_json(caminho + "moedas.json")

print("=== MÁQUINA DE BEBIDAS ===")

# Loop principal da aplicação
while True:
    modo = input("\nDigite 'admin' para modo administrador ou Enter para comprar: ").lower()
    if modo == "admin":
        if modo_admin(produtos, cedulas, moedas, caminho):
            break  # Encerra o programa se sair do modo admin
        continue

    if not produtos:
        print("Não há produtos cadastrados para venda.")
        exit()

    mostrar_produtos(produtos)
    produto = escolher_produto(produtos)
    qtd = solicitar_quantidade(produto)
    total = calcular_pagamento(produto["Preço"], qtd)

    # Processa o pagamento. A função irá encerrar o programa se não houver troco suficiente.
    cedulas, moedas = pagamento(total, cedulas, moedas)

    # Apenas atualiza o estoque e salva se o pagamento foi bem-sucedido (o programa não encerrou)
    produto["Estoque"] = str(int(produto["Estoque"]) - qtd)  # Atualiza o estoque

    # Salva os dados atualizados
    salvar_json(f"{caminho}produtos.json", produtos)
    salvar_json(f"{caminho}cedulas.json", cedulas)
    salvar_json(f"{caminho}moedas.json", moedas)

    if input("Deseja fazer nova operação? (s/n): ").lower() != "s":
        print("Programa encerrado.")
        break

# Mensagem final
print("\nAgradeçemos por utilizar! Desenvolvido por: Isabelle Duarte, Líbia Silveira e Sérgio Calazans.\n")
