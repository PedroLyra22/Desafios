import random                                                            # importa a biblioteca random

limitador_1 = int(input("Digite um número: "))                           # decide um dos limitadores
limitador_2 = int(input("Digite outro número: "))                        # decide um dos limitadores

numero_aleatorio = random.randrange(limitador_1, limitador_2)            # aleatoriza o número no intervalo

print("Um número aleatório no intervalo indicado é: ", numero_aleatorio) # imprime o número aleatório


