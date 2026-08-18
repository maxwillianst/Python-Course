print('======= Exercício aula 12 =======')
print('======= Binário / Octal / Hexadecimal =======')

n = int(input('Escreva um número: '))
print ('Qual base de conversão vc escolhe? \n1-Binário\n2-Octal\n3-Hexadecimal')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{n} em binário é {bin(n)[2:]}')

elif opcao == 2:
    print(f'{n} em octal é {oct(n)[2:]}')

elif opcao == 3:
    print(f'{n} em hexadecimal é {hex(n)[2:].upper()}')

else:
    print('Opção inválida!')