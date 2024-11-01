#Criando um programa para me perguntar em qual turno estudo. Digitar M-matutino, V-vespertino ou N-noturno. Imprima a mensagem "Bom dia!", "Boa tarde!", "Boa noite!" ou "Valor inválido!", conforme o caso.
#identificando turno
turno = "M", "V", "N"
turno = input('Digite o turno que você estuda: M para matutino, V para vespertino ou N para noturno:').upper()

if turno == "M":
    print("Bom dia! Em que posso ajudar?")
elif turno == "V":
    print("Boa tarde! Como estamos?")
elif turno == "N":
    print("Boa noite! Em que posso ser útil?")
else:
    print("Número Inválido!")