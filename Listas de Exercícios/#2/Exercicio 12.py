# Exercício 12

'''
12.	A partir das informações contidas na tabela abaixo, 
elabore um algoritmo que leia a massa em kg de um boxeador e mostre a qual categoria ele pertence. 
Caso ele não se encaixe, informe “Categoria inferior a Super-médio”. 
Lembrando que 1 quilograma = 2,20462262 libras. 

Massa                      Categoria
    201 lb ou mais           Peso-pesado
    176 até 201 lb           Cruzador
    169 até 175 lb           Meio-pesado
    161 até 168 lb           Super-médio

'''

# Entrada

massa = float(input("\nDigite a massa do boxeador em kg: (em Kg)"))

# Processamento
def classificarBoxeador(m): # m - massa

    # Conversão de kg para libras
    massaLb = m * 2.20462262
    
    if massaLb >= 201:
        return "Peso-pesado"
    elif 176 <= massaLb < 201:
        return "Cruzador"
    elif 169 <= massaLb < 176:
        return "Meio-pesado"
    elif 161 <= massaLb < 169:
        return "Super-médio"
    else:
        return "Categoria inferior a Super-médio"

# Saída

print(f"\nClassificação: {classificarBoxeador(massa)}.\n")
