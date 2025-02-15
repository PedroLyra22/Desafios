num = int(input("Digite um número: "))

def is_prime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

if is_prime(num):
    print("O número", num, "é primo")
else:
    print("O número", num,"não é primo")
