"""Implemente um programa que calcule e retorne a soma dos elementos de uma
matriz 5 x 5 de números inteiros."""

num=[]
for i in range(5):
    linha = []
    for j in range(5):
        linha.append(i)
    num.append(linha)
for linha in num :
    print(linha)