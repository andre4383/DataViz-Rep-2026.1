import random

print("Jogo da advinhação!")
n = random.randint(1,10)
palpite = int(input("Digite um numero entre 1 e 10: "))

print("Você digitou", palpite)

if palpite == n:
    print("Parabéns, você acertou!")
else:
    print("Você errou... O número certo era: ", n)

print("Fim de jogo!")