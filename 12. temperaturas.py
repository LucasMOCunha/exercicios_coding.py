#Programa para ler 5 temperaturas e exibir a menor, a maior e a média:

temperaturas = []

for i in range(5):
    temp = float(input(f"Digite a temperatura {i+1}: "))
    temperaturas.append(temp)

menor_temp = min(temperaturas)
maior_temp = max(temperaturas)
media_temp = sum(temperaturas) / len(temperaturas)

# Exibe os resultados
print(f"Menor temperatura: {menor_temp}")
print(f"Maior temperatura: {maior_temp}")
print(f"Média das temperaturas: {media_temp}")
