#Programa para calcular o crédito especial com base no saldo médio:

saldo_medio = float(input("Digite o saldo médio do último ano: R$ "))

if saldo_medio <= 200:
    credito = 0
    percentual = 0
elif saldo_medio <= 400:
    percentual = 0.20
    credito = saldo_medio * percentual
elif saldo_medio <= 600:
    percentual = 0.30
    credito = saldo_medio * percentual
else:
    percentual = 0.40
    credito = saldo_medio * percentual

print(f"\nSaldo médio: R$ {saldo_medio:.2f}")
print(f"Percentual de crédito: {percentual * 100:.0f}%")
print(f"Valor do crédito: R$ {credito:.2f}")