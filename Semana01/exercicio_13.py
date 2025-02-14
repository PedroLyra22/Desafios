num = int(input("Digite um número: "))
fat = 1

while num > 0:
    fat *= num
    num -= 1

print("O fatorial do número inserido é: ", fat)