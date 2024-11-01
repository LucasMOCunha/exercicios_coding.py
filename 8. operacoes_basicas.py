#Criando um programa que faça leitura de dois números e pergunte ao usuário qual operação básica (soma, subtração, multiplicação, divisão, exponenciação) ele deseja realizar. O resultado da operação deverá ser acompanhado de uma frase que diga se o número é: par ou ímpar; positivo ou negativo; inteiro ou decimal.

#Solicitando ao usuário que insira dois números
N1 = float(input("Digite o primeiro número desejado: "))
N2 = float(input("Digite o segundo número desejado: "))

#Solicitando a operação desejada
operacao = input("Qual operação básica você deseja realizar? 1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão, 5 - Exponenciação: ")

#Variável para armazenar o resultado da operação
resultado = None

#Executando a operação com base na escolha do usuário
if operacao == "1":
    resultado = N1 + N2
    print("Você escolheu somar!")
elif operacao == "2":
    resultado = N1 - N2
    print("Você escolheu subtrair!")
elif operacao == "3":
    resultado = N1 * N2
    print("Você escolheu multiplicar!")
elif operacao == "4":
    if N2 != 0:
        resultado = N1 / N2
        print("Você escolheu dividir!")
    else:
        print("Erro: Divisão por zero não é permitida.")
elif operacao == "5":
    resultado = N1 ** N2
    print("Você escolheu exponenciar!")
else:
    print("Operação inválida.")

#Verificando se o resultado foi calculado
if resultado is not None:
    #Exibindo o resultado
    print(f"Resultado: {resultado}")

    #Verificando se o número é par ou ímpar
    if resultado % 2 == 0:
        paridade = "par"
    else:
        paridade = "ímpar"

    #Verificando se o número é positivo ou negativo
    if resultado > 0:
        sinal = "positivo"
    elif resultado < 0:
        sinal = "negativo"
    else:
        sinal = "neutro"

    #Verificando se o número é inteiro ou decimal
    if resultado == int(resultado):
        tipo = "inteiro"
    else:
        tipo = "decimal"

    #Exibindo as características do resultado
    print(f"O resultado é um número {paridade}, {sinal} e {tipo}.")