print("**********************************")
print("Bem vindo no jogo de adivinhação!!")
print("**********************************")

numero_secreto = 42
total_de_tentativas = 5

for rodada in range(1,total_de_tentativas):
    #print("Tentativa", rodada, "de", total_de_tentativas)
    #print("Tentativa {} de {}" .format(rodada, total_de_tentativas))
    print(f"Tentativa {rodada} de {total_de_tentativas}")
    chute = input("Digite o seu número entre 1 e 100: ")
    chute = int(chute)
    print("Você digitou ", chute)
    
    if (chute < 1 or chute > 100):
        print("Você deve digitar um numero entre 1 e 100!!")
        continue

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

