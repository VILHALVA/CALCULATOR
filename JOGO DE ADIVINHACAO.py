from random import randint
from time import sleep

computador = randint(0,10)
print("😠Acabei de pensar em um número entre 0 e 10!")
sleep(2)

acertou = False
palpites = 0

while not acertou:
    jogador = int(input("😎Qual é o seu palpite?:\n>>>"))
    palpites += 1
    if jogador == computador:
        acertou = True
        resultado = f"👍ACERTOU!\n🔔Foram {palpites} Tentativas!"
    else:
        if jogador < computador:
            print(f"👎ERRADO!\n➕É MAIOR DO QUE {jogador}!")
        elif jogador > computador:
            print(f"👎ERRADO!\n➖É MENOR QUÊ {jogador}!!!")
                        
print(f"⭐Eu pensei no n° {computador}!\n⭐Você digitou: {jogador}!\n⭐RESULTADO:{resultado}")  