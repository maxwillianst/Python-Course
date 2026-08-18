print('======= Exercício aula 12 =======')
print('======= Média =======')

nota1 = float(input('Primeiro valor: '))
nota2 = float(input('Segundo valor: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Vc está reprovado!')
elif media >= 5 and media <= 6.9:
    print('Vc está de recuperação!')
else:
    print('Aprovado!')