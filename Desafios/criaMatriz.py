# implementar um código Python que cria uma matriz
# com as dimensões especificadas pelo usuário e a
# preenche com valor solicitado
nLinhas = int(input('Entre com a qtde de linhas: '))
nColunas = int(input('Entre com a qtde de colunas: '))
nPreencher = int(input('Entre com um valor inteiro para preencher: '))

def cria_matriz(linhas, colunas, valor):
    m = []
    for linha in range(linhas):
        linha_matriz = []
        for coluna in range(colunas):
            linha_matriz.append(valor)
        m.append(linha_matriz)

    for linha in range(linhas):
        for coluna in range(colunas):
            print(m[linha][coluna],end=' ')
        print('')
    
cria_matriz(nLinhas, nColunas, nPreencher)
