import random

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
senha = random.choices(numeros, k=8)

print("Senha aleatória gerada é: ", senha)