numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite outro número: "))
numero_3 = int(input("Digite mais um número: "))

maior = max(numero_1, numero_2, numero_3)
menor = min(numero_1, numero_2, numero_3)
meio = (numero_1 + numero_2 + numero_3) - (maior + menor)

print("O maior número é: ", maior)
print("O menor número é: ", menor)
print("O número do meio é: ", meio)