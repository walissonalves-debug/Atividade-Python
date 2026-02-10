n = int(input("Digite o valor de N (positivo): "))

if n <= 0:
    print("N deve ser um número inteiro positivo.")
else:
    h = 0.0  # Variável para armazenar o resultado da soma

    for i in range(1, n + 1):
        h += 1 / i

    print(f"O valor de H é: {h:.4f}")
