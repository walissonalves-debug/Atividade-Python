n = int(input("Digite um número inteiro N para calcular o fatorial: "))

fatorial = 1 #Criei uma variável e iniciei de 1

if n < 0:
    print("Não existe fatorial de número negativo.")
else:
    for i in range(1, n + 1): #esta função gera numero de 1 até n
        fatorial *= i #Em cada repetição, multiplica o valor atual de fatorial pelo valor de i.

    print(f"O fatorial de {n} é {fatorial}")
