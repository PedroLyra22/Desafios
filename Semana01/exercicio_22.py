import random

jogador_1 = random.randrange(1,6)
jogador_2 = random.randrange(1,6)

print("Resultado do jogador 1: ", jogador_1)
print("Resultado do jogador 2: ", jogador_2)

if jogador_1 > jogador_2:
    print("O vencedor é o jogador 1!")
else:
    if jogador_1 == jogador_2:
        print("Deu empate...")
    else:
        print("O vencedor é o jogador 2!")
