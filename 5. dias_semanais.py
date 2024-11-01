#Criando um programa que leia um número e exiba o dia correspondente da semana. Se digitado outro número, retornar uma mensagem informando valor inválido.
dias = "1234567"
num = input("Digite o número correspondente para o dia desejado: 1 - Domingo, 2 - Segunda, 3 - Terça, 4 - Quarta, 5 - Quinta, 6 - Sexta, 7 - Sábado:")

if num in dias:
    print("Dia confirmado! Obrigado pela preferência!")
else:
    print("Número inválido! Tente novamente...")