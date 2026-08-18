print('======= Exercício aula 12 =======')
print('======= CÁLCULO DO TRIÂNGULO =======')

r1 = int(input('Primeiro lado: '))
r2 = int(input('Segundo lado: '))
r3 = int(input('Terceiro lado: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:

    if r1 == r2 == r3:
        print('Será formado um triângulo Equilátero')

    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Será formado um triângulo Isósceles')

    else:
        print('Será formado um triângulo Escaleno')

else:
    print('Não consegue formar um triângulo')
