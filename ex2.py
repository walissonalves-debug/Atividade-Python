"""Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais
elementos. Escreva ao final a matriz obtida."""

num=[]
for i in range(5):
    linha = []
    for j in range(5):
        linha.append(1)
    num.append(linha)
for linha in num :
    print(linha)