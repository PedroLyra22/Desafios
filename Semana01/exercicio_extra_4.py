numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite outro número: "))
numero_3 = int(input("Digite mais um número: "))

if (numero_1 > numero_2):
    if (numero_1 > numero_3):
        print("O maior número é: ", numero_1)
    else:
        print("O maior número é: ", numero_3)
else:
    if (numero_2 > numero_3):
        print("O maior número é: ", numero_2)
    else:
        print("O maior número é: ", numero_3)
