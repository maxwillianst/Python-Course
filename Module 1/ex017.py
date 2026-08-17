import math
print('======= Exercício aula 08 =======')
print('======= HIPOTENUSA =======')

op = float(input('Qual o comprimento do Cateto Oposto? '))
ad = float(input('Qual o comprimento do Cateto Adjcente? '))
hipo = math.hypot(op, ad)
print('O comprimento da Hipotenusa é {:.2f}'.format(hipo))


