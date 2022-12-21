'''
10) Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a 
quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante 
perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o 
total de dias.
'''
cigarro_dia = int(input("Quantidade de cigarros por dia: "))
anos_fumando = int(input("Quantidade de anos fumando: "))

anos_de_vida = ((10/60)/24)*cigarro_dia*anos_fumando*365
print(f'Total de dias perdidos pelo ciggaro {anos_de_vida: .2f}')
