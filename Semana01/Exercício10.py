valor_inicial = float(input("Insira o valor de um produto: ")) # solicitação do valor inicial
desconto = float(input("Insira o desconto do produto: "))      # solicitação do desconto

valor_final = (valor_inicial - desconto) / 100 * 100           # cálculo do valor com desconto

print("Valor final com desconto é: ", valor_final)             # impressão do valor final