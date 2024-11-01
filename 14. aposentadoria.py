#Programa para calcular o ano de aposentadoria

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

ano_atual = 2024
ano_aposentadoria = ano_atual + (65 - idade)

if idade < 65:
    print(f"{nome}, você poderá se aposentar em {ano_aposentadoria}.")
else:
    print(f"{nome}, você já pode se aposentar!")
