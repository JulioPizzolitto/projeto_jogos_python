print("**********************************")
print("Bem vindo no jogo de adivinhação!!")
print("**********************************")

numero_secreto = 42
total_de_tentativas = 5
rodada = 1

while(rodada <= total_de_tentativas):
    #print("Tentativa", rodada, "de", total_de_tentativas)
    #print("Tentativa {} de {}" .format(rodada, total_de_tentativas))
    print(f"Tentativa {rodada} de {total_de_tentativas}")
    chute = input("Digite o seu número: ")
    chute = int(chute)
    print("Você digitou ", chute)

    acertou = numero_secreto == chute
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Você acertou!!")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")
    rodada = rodada + 1

print("Fim do jogo.")

