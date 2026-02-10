contador = 0
par=0
impar=0
for i in range(1,10):
    valor = int(input("informe um número: "))
    if valor % 2 == 0:
        par += 1
        

    if valor % 2 != 0:
        impar += i

print(f"A soma de todos os números pares é: {par}")
print(f"A soma de todos os números impares é: {impar}")
    
    