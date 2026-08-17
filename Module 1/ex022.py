print('======= Exercício aula 09 =======')
print('======= LEITOR DE NOME =======')

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome maiúsculo é: {}'.format(nome.upper()))
print('Seu nome minúsculo é: {}'.format(nome.lower()))
print('Seu nome tem ao todo: {} letras!'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem: {} letras!'.format(nome.find(' ')))

