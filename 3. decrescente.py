#Criando um programa que leia três números e mostre-os em ordem descrescente.

numeros = []

#inicia um loop "for" / "i" significa o indice de repetições
for i in range(3):
    num = int(input("Digite um número:"))
    numeros.append(num)

#sort(reverse=True) ordena os números em ordem decrescente
numeros.sort(reverse=True)
print(numeros)