import datetime

hora_atual = int(input("Digite a hora atual: "))
minuto_atual = int(input("Digite o minuto atual: "))
segundo_atual = int(input("Digite o segundo atual: "))

fuso = hora_atual + 5

if fuso >= 24:
    fuso -= 24
    horario = datetime.time(fuso, minuto_atual, segundo_atual)
    print("A hora no outro país é: ", horario)
else:
    horario = datetime.time(fuso, minuto_atual, segundo_atual)
    print("A hora no outro país é: ", horario)



