# Desafio do Jogo da Forca

# Entrada

import random as rd

'''
- Faça um jogo da forca, usando de base 
- implementar função para separar as letras da resposta
- A vida é determinada pela quantidade de letras
- No começo de jogo, 
- Cada erro de letra, perde vida e aparece uma dica (no máximo duas dicas)
- 
'''

def jogo():

    palavras = {
        # chave: ["Resposta", "Dica 1", "Dica 2"]
        0: ["Sao Paulo", "Time de futebol brasiileiro tricampeão mundial.", "É um time de uma cidade paulistana"],
        1: ["Flamengo", "Maior torcida do Brasil", "Eliminou o Grêmio na Libertadores de 2019 na semifinal."],
        2: ["Parana", "Surgiu de uma fusão de dois times em 1989", "É um time paranaense."],
        3: ["Paris Saint Germain", "Já teve em seu time o Ronaldinho Gaúcho", "Muito se fala a sua sigla como nome do time"]
    }

    pontos = 0
    ordem_jogo = []

    for valor in palavras.keys():

        ordem_jogo.append(valor)

    rd.shuffle(ordem_jogo)

    i = 1
    for valor in ordem_jogo:

        print(f"\nPergunta {i}: {palavras[valor][1]}")
        resposta = str(input("Qual é a resposta? "))

        if resposta == palavras[valor][0]:

            pontos += 1
            print("\nVocê acetou! Ganhou 1 ponto pela resposta.")
        
        else:

            print(f"\nVocê errou, tente novamente. Dica: {palavras[valor][2]}")
            resposta = str(input("Qual é a resposta? "))

            if resposta == palavras[valor][0]:

                pontos += 0.5
                print("\nVocê acetou! Ganhou meio ponto pela resposta.")
            
            else:

                print(f"\nVocê errou! A resposta era: {palavras[valor][0]}")
        
        i += 1
        
    print(f"\nPontuação final: {pontos}\n")

jogo()