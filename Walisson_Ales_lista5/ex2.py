vetor = []

quadrado = []

for i in range(0,10):
    vetor.append(float(input("Digite o valor da posição {}: ".format(i))))

for i in range(0,10):
    quadrado.append(vetor[i]**2)

print("Vetor: ",vetor)
print("Vetor ao quadrado: ",quadrado)
