print('======= Exercício aula 09 =======')
print('======= LEITOR DE fRASE =======')

nome = str(input('Digite seu nome completo: ')).strip()
no = nome.split()
print('Olá, {}'.format(nome))
print('Seu primeiro nome é: {}'.format(no[0]))
print('Seu último nome é: {}'.format(no[len(no)-1]))