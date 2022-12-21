'''
8) Converta uma temperatura digitada em Fahrenheit para Celsius . F = 9*C/5 + 32
'''
f = float(input('Temperatura ºF: '))
c = (f-32)*5/9

print(f'{f: .1f}ºF equivale a {c: .1f}C')
