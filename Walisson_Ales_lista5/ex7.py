vetor = []

for i in range(0,5):
    vetor.append(float(input(f"Informe o {i+1}º valor: ")))

codigo = int(input("Informe o código: "))

if codigo == 0:
    print("Programa finalizado.")
elif codigo == 1:
    print(vetor)
elif codigo == 2:
    print(vetor.reverse())
else:
    print("Código inválido.")