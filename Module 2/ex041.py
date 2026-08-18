print('======= Exercício aula 12 =======')
print('======= Natação =======')

dataNascimento = int(input('Informe o ano de nascimento: '))
ano = 2026
idade = ano - dataNascimento
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 20:
    print('Sênior')
else:
    print('Master')