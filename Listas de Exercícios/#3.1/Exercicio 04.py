# Exercício 4

'''
4.	Faça um programa que peça dois números, base e expoente, 
calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem.
'''

# ENTRADA
base = int(input("\nDigite a base: "))
expoente = int(input("Digite o expoente: "))
resultado = 1

# PROCESSAMENTO

# Loop FOR que se repetirá vezes o valor absoluto do expoente
for _ in range(abs(expoente)): 
    resultado *= base # Multiplica resultado pela base repetidamente

if expoente < 0: # Verifica se o expoente é negativo
    resultado = 1 / resultado

# SAÍDA
print(f"\n{base} elevado a {expoente} é igual a {resultado}")
