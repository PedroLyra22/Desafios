import datetime

dia_1 = int(input("O dia da primeira data: "))
mes_1 = int(input("O mes da primeira data: "))
ano_1 = int(input("O ano da primeira data: "))

dia_2 = int(input("O dia da primeira data: "))
mes_2 = int(input("O mes da primeira data: "))
ano_2 = int(input("O ano da primeira data: "))

data_1 = datetime.datetime(day=dia_1, month=mes_1, year=ano_1)
data_2 = datetime.datetime(day=dia_2, month=mes_2, year=ano_2)

difereca = data_2 - data_1

print("Os dias de diferença são: ", difereca)