print('======= Exercício aula 10 =======')
print('======= CALCULO DE SALÁRIO =======')

salario = float(input('Qual o seu salario: '))
if salario <= 1250:
    print('Seu novo salário é de: R$ {:.2f}'.format(salario * 1.15))
else:
    print('Seu novo salário e de: R$ {:.2f}'.format(salario * 1.10))
