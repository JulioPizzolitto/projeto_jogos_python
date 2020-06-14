import random

def jogar():
    print("**********************************")
    print("Bem vindo no jogo de adivinhação!!")
    print("**********************************")

    # numero_secreto = round(random.random() * 100)
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas):
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute = input("Digite o seu número entre 1 e 100: ")
        chute = int(chute)
        print("Você digitou ", chute)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um numero entre 1 e 100!!")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print(f"Você acertou e fez {pontos} pontos!!")
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
                if (rodada == total_de_tentativas):
                    print(f"O número secreto era {numero_secreto}. Você fez {pontos}")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
                if (rodada == total_de_tentativas):
                    print(f"O número secreto era {numero_secreto}. Você fez {pontos}")
            pontos_perdidos = abs(numero_secreto - chute)
            type(pontos_perdidos)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo.")

if(__name__ == "__main__"):
    jogar()