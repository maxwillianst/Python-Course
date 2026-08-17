print('======= Exercício aula 07 =======')
print('======= LOCADORA =======')

km = float(input('Qual a quantidade de KM percorrido?' ))
dias = int(input('Quantos dias? '))
pago = (km * 0.15) + (dias * 60)
print('O valor a se pagar é R${:.2f} '.format(pago))


