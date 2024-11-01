#Criando um programa que peça um número correspondente a um determinado ano e informando na sequência se o ano é ou não bissexto.
#Solicitando ao usuário que insira um ano
ano = int(input("Digite o ano que deseja verificar: "))

#Verifica se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")