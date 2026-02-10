n = int(input("Digite o número de termos da série de Fibonacci: "))

# Termos iniciais
a = 1
b = 1

print("Série de Fibonacci:")

for i in range(n):
    print(a, end=' ')

    a, b = b, a + b
