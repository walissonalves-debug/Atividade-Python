maior  = 0
menor = 99999

num = int(input("Informe quantas repetições: "))
for i in range(1, num+1):
    valor = int(input("informe um numero: "))
    if (valor>maior):
        maior = valor
    if (valor<menor):
        menor = valor
        
print ("O maior numero é: ", maior)
print ("O menor numero é: ", menor)             