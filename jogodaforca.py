#Este é um projeto criado por Louyse para praticar as funções e o uso da linguagem Python.

import random

# Define um conjunto de palavras secretas
palavras_secretas = ["banana", "maçã", "pera", "uva"]

# Gera uma palavra secreta aleatória
palavra_secreta = random.choice(palavras_secretas)

# Inicializa um contador de erros
erros = 0

# Desenha o enforcado
print("_" * len(palavra_secreta))

# Loop principal do jogo
while erros < len(palavra_secreta) + 1:
    # Solicita uma letra ao jogador
    letra = input("Digite uma letra: ")

    # Verifica se a letra está correta
    if letra in palavra_secreta:
        # Atualiza a tela com a letra correta
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                print(letra, end="")
            else:
                print("_", end="")
    else:
        # Adiciona um erro
        erros += 1

        # Desenha o enforcado
        print()
        for i in range(erros):
            print(" |")
        print(" |")
        print(" |")
        if erros == 1:
            print("   ()")
        elif erros == 2:
            print("   (O)")
        elif erros == 3:
            print("   (O)")
            print("   |")
        elif erros == 4:
            print("   (O)")
            print("   |")
            print("   /")
        elif erros == 5:
            print("   (O)")
            print("   |")
            print("   / \\")
        elif erros == 6:
            print("   (O)")
            print("   |")
            print("   / \\")
            print("   -")

    # Verifica se o jogo terminou
    if erros == len(palavra_secreta) + 1:
        print("Você perdeu!")
        print("A palavra secreta era", palavra_secreta)
    else:
        if palavra_secreta == "".join(letra for letra in palavra_secreta):
            print("Você ganhou!")