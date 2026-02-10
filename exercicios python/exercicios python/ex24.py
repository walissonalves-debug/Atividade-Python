votos_a = 0
votos_b = 0
votos_c = 0
votos_branco = 0
votos_nulo = 0

total_eleitores = 20
voto_num = 1

print("==== Eleição: Votação com 20 eleitores ====")
print("Opções de voto:")
print("1 - Candidato A")
print("2 - Candidato B")
print("3 - Candidato C")
print("4 - Voto em Branco")
print("5 - Voto Nulo")

while voto_num <= total_eleitores:
    
        voto = int(input(f"\nEleitor {voto_num}, digite seu voto (1 a 5): "))

        if voto == 1:
            votos_a += 1
            voto_num += 1
        elif voto == 2:
            votos_b += 1
            voto_num += 1
        elif voto == 3:
            votos_c += 1
            voto_num += 1
        elif voto == 4:
            votos_branco += 1
            voto_num += 1
        elif voto == 5:
            votos_nulo += 1
            voto_num += 1
        else:
            print("⚠️ Voto inválido. Digite um número entre 1 e 5.")
    
        print("⚠️ Entrada inválida. Digite apenas números inteiros.")

# Exibe o relatório final
print("\n===== RESULTADO DA VOTAÇÃO =====")
print(f"Total de votos para Candidato A: {votos_a}")
print(f"Total de votos para Candidato B: {votos_b}")
print(f"Total de votos para Candidato C: {votos_c}")
print(f"Total de votos em Branco: {votos_branco}")
print(f"Total de votos Nulos: {votos_nulo}")

# Verifica o vencedor ou empate
maior_voto = max(votos_a, votos_b, votos_c)
vencedores = []

if votos_a == maior_voto:
    vencedores.append("Candidato A")
if votos_b == maior_voto:
    vencedores.append("Candidato B")
if votos_c == maior_voto:
    vencedores.append("Candidato C")

if len(vencedores) == 1:
    print(f"\n🎉 {vencedores[0]} foi o vencedor com {maior_voto} votos!")
else:
    print(f"\n⚠️ Houve empate entre: {', '.join(vencedores)} com {maior_voto} votos cada.")
