valores = []

for i in range(0,6):
    valores.append(int(input(f"Informe o {i+1}º valor: ")))

    valores.reverse()   
    
print(valores)