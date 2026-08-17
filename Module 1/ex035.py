print('======= Exercício aula 10 =======')
print('======= CALCULO DO TRIÂNGULO =======')

r1 = int(input('Primeiro lado: '))
r2 = int(input('Segundo lado: '))
r3 = int(input('Terceiro lado: '))
if  r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Consegue ser um triangulo')
else:
    print('Não consegue')