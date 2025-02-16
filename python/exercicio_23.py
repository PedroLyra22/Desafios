import math

num = (input("Digite um número: "))

raiz = math.sqrt(num)

print(raiz)

if raiz == float(raiz):
    print("A raíz quadrada de ", num, " é exata")
else:
    print("A raíz quadrada de ", num, "não é exata!")