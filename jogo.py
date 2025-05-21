import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")

    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("Tente um número maior.")
        elif palpite > numero_secreto:
            print("Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
            break

jogo_adivinhacao()