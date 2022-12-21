'''
9) Escreva um programa que pergunte a quantidade de km percorridos por um carro
alugado pelo usuário, assim como a quantidade de dias pelos quais o carro
foi alugado. Calcule o preço a pagar,sabendo que o carro custa R$ 60,00
por dia e R$ 0,15 por km rodado.

'''
km = float(input('Distância percorrida Km: '))
dia = int(input('Quantidade de dias de locação: '))
valor = 60*dia + 0.15*km

print(f'Valor total do aluguel:{valor: .2f}R$')
