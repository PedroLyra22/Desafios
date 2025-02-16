from collections import Counter
import re

texto = input("Digite um texto: ")

lista_palavras = re.findall(r"\b\w+\b", texto)
contagem_palavras = Counter(lista_palavras)

print(contagem_palavras)