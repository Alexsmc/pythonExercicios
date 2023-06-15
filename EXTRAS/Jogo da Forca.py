def jogar_forca(palavra_secreta):
    tentativas_maximas = 6
    tentativas = 0
    letras_corretas = []
    letras_erradas = []

    while tentativas < tentativas_maximas:
        letra = input("Digite uma letra: ")

        if letra in palavra_secreta:
            letras_corretas.append(letra)
        else:
            letras_erradas.append(letra)
            tentativas += 1

        # Verifica se o jogador ganhou
        if all(letra in letras_corretas for letra in palavra_secreta):
            print("Parabéns! Você acertou a palavra:", palavra_secreta)
            return

        # Imprime as tentativas restantes como bolinhas
        print("Tentativas restantes:", end=" ")
        print(" * " * (tentativas_maximas - tentativas))

        # Imprime a palavra secreta com as letras corretas reveladas
        progresso = ""
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_corretas:
                progresso += letra_secreta + " "
            else:
                progresso += "_ "
        print("Progresso: ", progresso)

        # Mostra as letras erradas
        print("Letras erradas:", letras_erradas)

    print("Game over! A palavra era:", palavra_secreta)

# Palavra a ser adivinhada
palavra = "python"

# Inicia o jogo
jogar_forca(palavra)
