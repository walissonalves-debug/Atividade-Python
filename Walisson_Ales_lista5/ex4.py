valor =[]

for i in range(0,15):
    valor.append (int(input((f"Informe o {i+1}º número: "))))

maior = max(valor)
menor = min(valor)

pos_maior = valor.index(maior)
pos_menor = valor.index(menor)

# mostra os resultados
print(f"\nMaior valor: {maior} (posição {pos_maior})")
print(f"Menor valor: {menor} (posição {pos_menor})")