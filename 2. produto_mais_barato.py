#Criando um programa que pergunte o valor de 3 produtos e me informe qual é o mais viável, sempre optando pelo mais barato.

#valores
P1 = float(input("Insira o valor do produto:"))
print(f"O valor é de {P1}")
P2 = float(input("Insira o valor do produto:"))
print(f"O valor é de {P2}")
P3 = float(input("Insira o valor do produto:"))
print(f"O valor é de {P3}")

#comparando
if P1 < P2 and P1 <  P3:
 print(f"O valor do {P1} é o mais barato.")
elif P2 < P1 and P2 < P3:
 print(f"O valor do {P2} é o mais barato.")
else:
 print(f"O valor do {P3} é o mais barato")