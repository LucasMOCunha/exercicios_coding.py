#Programa para cálculo da folha de pagamento:
valor_hora = float(input("Digite o valor da sua hora (R$): "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas

desconto_ir = 0.0

if salario_bruto <= 2112.00:
    desconto_ir = 0.0  #Isento
elif salario_bruto <= 3751.05:
    desconto_ir = salario_bruto * 0.15  #15%
elif salario_bruto <= 4664.68:
    desconto_ir = salario_bruto * 0.225  #22.5%
else:
    desconto_ir = salario_bruto * 0.275  #27.5%

#Calculando o desconto do Sindicato (3%)
desconto_sindicato = salario_bruto * 0.03

#Calculando o salário líquido
salario_liquido = salario_bruto - (desconto_ir + desconto_sindicato)

#Calculando o FGTS (11% do salário bruto, não descontado)
fgts = salario_bruto * 0.11

print(f"\nSalário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto do Imposto de Renda: R$ {desconto_ir:.2f}")
print(f"Desconto do Sindicato (3%): R$ {desconto_sindicato:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
print(f"Depósito do FGTS (11%): R$ {fgts:.2f}")