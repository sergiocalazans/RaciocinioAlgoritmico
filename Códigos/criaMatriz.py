# implementar um código Python que cria uma matriz
# com as dimensões especificadas pelo usuário e a
# preenche com valor 1
m = []
nlinhas = int(input('Entre com a qtde de linhas: '))
ncolunas = int(input('Entre com a qtde de colunas: '))
#5 x 9

for linha in range(nlinhas):
    linha_matriz = []
    for coluna in range(ncolunas):
        linha_matriz.append(1)
    m.append(linha_matriz)

m[3][2] = 10

for linha in range(nlinhas):
    for coluna in range(ncolunas):
        print(m[linha][coluna],end=' ')
    print('')