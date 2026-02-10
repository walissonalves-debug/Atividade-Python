"""Implemente um programa que calcule a soma dos elementos de cada linha e
coluna de uma matriz e armazene os resultados em vetores. Ao final, exiba o valor
do somatório das linhas e das colunas armazenados nos vetores."""

matriz=[]
soma=0

for i in range (3):
    linha = []
    for j in range(3):
        linha.append(i)
    matriz.append(linha)
    
soma_linha =[]    
for i in range(3):
    soma = 0
    for j in range(3):
        soma+= matriz[i][j]
        soma_linha.append(soma)
for linha in matriz :
    print(soma_linha)
    





