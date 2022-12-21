'''
5) Solicite o preço de uma mercadoria e o percentual de desconto.
Exiba o valor do desconto e o preço a pagar.

'''

p = float(input("Preço da mercadoria R$: "))
d = float(input("Preço do desconto %: "))
desconto = (d/100)*p
preço = p - desconto

print(f"Desconto: R${desconto: .2f}")
print(f"Preço a pagar: R${preço: .2f}")
