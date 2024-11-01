#Programa que lê 5 números e informa a soma e a média

numeros = []  #Lista para armazenar os números

#Lendo os 5 números do usuário
for i in range(5):
    numero = float(input(f"Digite o número {i+1}: "))
    numeros.append(numero)  #Adicionando o número à lista

#Calcula a soma e a média
soma = sum(numeros)
media = soma / len(numeros)

#Exibe a soma e a média
print(f"Soma dos números: {soma}")
print(f"Média dos números: {media}")
