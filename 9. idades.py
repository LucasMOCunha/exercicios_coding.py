# Criando um programa que peça a idade e exiba a informação.
# Os valores aceitáveis devem estar entre 0 e 150.
# Valores fora desse limite não poderão ser aceitos.

idade = int(input("Qual a sua idade?: "))

if 0 <= idade <= 150:
    print("Obrigado por informar sua idade!")
else:
    print("Valor incorreto! Tente novamente!")
