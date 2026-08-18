print('======= Exercício aula 12 =======')
print('======= Alistamento =======')

ano = int(input('Qual o ano do seu nascimento? '))
anoatual = 2026
calculo = anoatual - ano
falta = 18 - calculo
faz = calculo - 18
if calculo < 18:
    print(f'Falta {falta} ano(s) pra vc se alistar!')
elif calculo == 18:
    print('Já está na hora de se alistar!')
else:
    print(f'Já faz {faz} anos que vc se alistou!')
