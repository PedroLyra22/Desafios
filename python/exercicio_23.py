import math

num = int(input("Digite um número: "))

raiz = math.sqrt(num)

if raiz == int(raiz):
    print("A raíz quadrada de ", num, " é exata")
else:
    print("A raíz quadrada de ", num, "não é exata!")