"""Implemente um programa que verifique se uma matriz 2 x 3 é simétrica, ou seja,
se é igual à sua transposta. Ao final, retorne se a matriz é transposta ou não."""

"""matriz =[]
for i in range(2):
    linha = []
    for j in range(3):
        linha.append(i)
matriz.append(linha)    

print(linha)"""

matriz = []
for i in range(2):
    linha = []
    for j in range(3):
        linha.append(1)
    matriz.append(linha)
for linha in matriz:
    print(linha)

transposta =[]
for j in range(3):
    linha1 = []
    for i in range(2):
        linha1.append(2)
    transposta.append(linha1)
for linha1 in transposta :
    print(linha1)

#verificando se são simétricas:
simetrica = matriz== transposta

if simetrica:
    print("A matriz é simétrica")
else:
    print("A matriz não é simétrica")