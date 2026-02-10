# Leitura do número de termos
n = int(input("Digite o número de termos da série de Ricci: "))

if n < 3:
    print("A série de Ricci precisa de pelo menos 3 termos.")
else:
    a = int(input("Digite o primeiro termo: "))
    b = int(input("Digite o segundo termo: "))

    print("Série de Ricci:")
    print(a, b, end=' ')
    soma = a + b

    for i in range(3, n + 1):
        proximo = a + b
        print(proximo, end=' ')
        soma += proximo
        a, b = b, proximo

    print(f"\nSoma dos termos: {soma}")
