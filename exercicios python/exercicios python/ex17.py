n = int(input("Infore um número: "))

print(f"Divisores de {n}:")

for i in range(1, n + 1):
    if n % i == 0:
        print(i)
