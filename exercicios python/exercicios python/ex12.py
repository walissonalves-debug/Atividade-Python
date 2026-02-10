maior = 0
menor = 99999

for i in range (1,11):
    valor = int(input("Informe um número: "))
    
    if (valor>maior):
        maior = valor
    
    if (valor<menor):
        menor = valor
        
print ("O maior numero é: ", maior)
print ("O menor numero é: ", menor)
