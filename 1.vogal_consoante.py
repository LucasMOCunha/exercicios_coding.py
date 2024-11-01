#Criando programa para verificar se a letra digitada é vogal ou consoante.
vogal = "aeiou"
letra = input("Digite a letra:")

#verificando de forma simplificada
if letra in vogal:
    print("A letra é uma vogal!")
else:
   print("A letra é uma consoante!")

#verificando de forma mais extensa
if letra == 'a':
  print("A letra digitada é uma vogal")
elif letra == 'e':
  print("A letra digitada é uma vogal")
elif letra == 'i':
  print("A letra digitada é uma vogal")
elif letra == 'o':
  print("A letra digitada é uma vogal")
elif letra == 'u':
  print("A letra digitada é uma vogal")
else:
  print("A letra é uma consoante")