'''
4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o
valor do salário e a porcentagem do aumento. Exiba o valor do aumento e
do novo salário.

'''
salario = float(input("Salario R$: "))
aumento = float(input("Aumento %: "))
aumento_real = salario*(aumento/100)
novo_salario = salario + salario*(aumento/100)

print(f'Aumento de R${aumento_real: .2f}')
print(f"Novo salario de: R${novo_salario: .2f}")
