import forca
import adivinhacao
print("********************************")
print("*****  Escolha seu jogo!!  *****")
print("********************************")

print("(1) Forca \n(2) Advinhação")

jogo = int(input("Qual jogo?? "))

if (jogo == 1):
    print("Jogando forca")
    forca.jogar()
elif (jogo == 2):
    print("Jogando adivinhação")
    adivinhacao.jogar()
