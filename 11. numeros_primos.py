#Programa para verificar se um número é primo:

numero = int(input("Digite um número inteiro: "))

eh_primo = True

if numero < 2:
    eh_primo = False
else:
    #Verificando a divisibilidade de 2 até a raiz quadrada do número
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:  #Se o número é divisível por i, então não é primo
            eh_primo = False
            break  #Encerra o laço assim que encontra um divisor

if eh_primo:
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
