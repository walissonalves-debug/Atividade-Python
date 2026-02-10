numeros = []
pares = []
impares = []

for i in range(0,10):
    numeros.append(int(input(f"Informe o {i+1}º número: ")))


for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

soma_pares = 0
for i in pares:
    soma_pares += i
    
quantidade_impares = 0
for i in impares:
    quantidade_impares += 1
# Nenhum código adicional é necessário aqui, pois a lógica já foi feita sem usar fórmulas ("formula" no sentido de funções prontas tipo sum, len, etc).

print(f"Os números pares digitados são: {pares}")
print(f"A soma dos números pares digitados é: {soma_pares}")
print(f"Os números ímpares digitados são: {impares}")
print(f"A quantidade de números ímpares digitados é: {quantidade_impares}")