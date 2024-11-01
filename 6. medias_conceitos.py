#Criando um programa para leitura de duas notas parciais obtidas ao longo de um semestre, e calculando a média obedecendo às regras de atribuição de conceitos.

#notas semestrais
nota1 = int(input("Digite a primeira nota do aluno:"))
nota2 = int(input("Digite a segunda nota do aluno:"))
soma = nota1 + nota2
print(soma)

#calculando a média para atribuir o conceito
media = soma / 2
print(media)

conceitoA = (9, 10)
conceitoB = (7.5, 9)
conceitoC = (6, 7.5)
conceitoD = (4, 6)
conceitoE = (0, 4)

def verificar_conceito(media):
    if conceitoA[0] <= media <= conceitoA[1]:
        print("Parabéns! Aluno aprovado por média! Conceito A!")
    elif conceitoB[0] <= media < conceitoB[1]:
        print("Parabéns! Aluno aprovado por média! Conceito B!")
    elif conceitoC[0] <= media < conceitoC[1]:
        print("Parabéns! Aluno aprovado por média! Conceito C!")
    elif conceitoD[0] <= media < conceitoD[1]:
        print("Ops! Infelizmente, aluno reprovado por média! Conceito D!")
    elif conceitoE[0] <= media < conceitoE[1]:
        print("Ops! Infelizmente, aluno reprovado por média! Conceito E!")
    else:
        print("Número inválido!")

#Teste da função
media = 8.5
verificar_conceito(media)