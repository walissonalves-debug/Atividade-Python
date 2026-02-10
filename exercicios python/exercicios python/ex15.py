def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a
a = int(input("Digite o valor de A (inteiro e positivo): "))
b = int(input("Digite o valor de B (inteiro e positivo): "))

if mdc(a, b) == 1:
    print("A e B são primos entre si.")
else:
    print("A e B NÃO são primos entre si.")
