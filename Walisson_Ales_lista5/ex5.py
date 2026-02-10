notas = []
soma = 0

for i in range(0,15):
    notas.append(float(input(f"Informe a nota do {i+1}º aluno: ")))
    soma += notas[i]

media = soma/15 



print(f"A média geral das notas é: {media:.2f}")