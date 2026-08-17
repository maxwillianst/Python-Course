print('======= Exercício aula 10 =======')
print('======= ADIVINHAR O NÚMERO =======')
import random

n = int(input('Qual o número que o computador escolheu? '))
es = random.randint(0, 5)
if n == es:
    print('Acertou!')
else:
    print('Errou!')
