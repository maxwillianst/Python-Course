print('======= Exercício aula 10 =======')
print('======= ANO BISSEXTO =======')

ano = int(input('Digite algum ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano bissexto'.format(ano))
else:
    print('Não e um ano bissexto')