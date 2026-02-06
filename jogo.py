import random

numero_secreto = random.randint(1, 10)
tentativas = 0
acertou = False

print("Jogo de Adivinhação")
print("Tente adivinhar o número entre 1 e 10")

while not acertou:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite < numero_secreto:
        print("Número muito baixo")
    elif palpite > numero_secreto:
        print("Número muito alto")
    else:
        print("Parabéns! Você acertou!")
        print("Tentativas:", tentativas)
        acertou = True
