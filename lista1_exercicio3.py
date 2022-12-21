'''
3) Escreva um programa que leia a quantidade de dias, horas, minutos e
segundos do usuário. Calcule o total em segundos

'''
d = int(input("Dias: "))
h = int(input("Horas: "))
m = int(input("Minutos: "))
s = int(input("Segundos: "))

print(d*86400 + h*3600 + m*60 + s)
