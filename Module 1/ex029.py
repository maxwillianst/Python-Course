print('======= Exercício aula 10 =======')
print('======= MULTA =======')

velocidade = int(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print('Você recebeu uma multa de {}'.format((velocidade - 80) * 7))
else:
    print('Ok')


