
soma = 0   
for i in range (1,6):
    numeros = float(input("Digite o preço: "))
    soma += numeros

    if soma >= 100:
        soma *= 0.9
        break

print(f"O valor do desconto é de R$ {soma:.2f}")