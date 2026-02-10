conjunto1 = []
conjunto2 = []

for i in range(0,5):
    conjunto1.append(float(input(f"Informe o {i+1}º valor do conjunto 1: ")))
    conjunto2.append(float(input(f"Informe o {i+1}º valor do conjunto 2: ")))

produto_escalar = 0

for i in range(0,5):
    produto_escalar += conjunto1[i] * conjunto2[i]

print(f"O produto escalar entre os conjuntos é: {produto_escalar}")