# Exercício 9

'''
9.	Faça um programa que leia uma quantidade indeterminada de números positivos, 
encerrando quando a entrada for -1 e conte quantos deles estão nos 
seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
'''

# ENTRADA e PROCESSAMENTO

intervalos = [0, 0, 0, 0]

while True:
        num = int(input("Digite um número positivo (-1 para sair): "))
        if num == -1:
            break
        if 0 <= num <= 25:
            intervalos[0] += 1
        elif 26 <= num <= 50:
            intervalos[1] += 1
        elif 51 <= num <= 75:
            intervalos[2] += 1
        elif 76 <= num <= 100:
            intervalos[3] += 1

# SAÍDA
print(f"\n[0-25]: {intervalos[0]}, [26-50]: {intervalos[1]}, [51-75]: {intervalos[2]}, [76-100]: {intervalos[3]}\n")
