print('======= Exercício aula 10 =======')
print('======= CALCCULO DE VALOR POR KM =======')

dis = int(input('Quantos KM vc percorreu? '))
if dis <= 200:
    print('Você deve R${} '.format(dis * 0.50))
else:
    print('Você deve R${} '.format(dis * 0.45))