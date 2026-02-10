acum = 0
media = 0
contador = 0
for i in range(1,101):
    acum = acum + i
    contador = contador + 1 
    print(i)
media = acum/contador
print(f"A media é {media}")