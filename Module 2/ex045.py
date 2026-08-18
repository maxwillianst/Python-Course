from random import randint
('======= Exercício aula 12 =======')
print('======= Jokenpô =======')

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('Suas opções:\n'
      '[ 0 ] Pedra\n'
      '[ 1 ] Papel\n'
      '[ 2 ] Tesoura')
jogador = int(input('Qual sua jogada? '))
print('-=' * 12)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 12)
if computador == 0:
    if jogador == 0:
            print('EMPATE')
    elif jogador == 1:
            print('JOGADOR VENCEU')
    elif jogador == 2:
            print('COMPUTADOR VENCEU')
    else:
            print('Jogada Inválida')
elif computador == 1:
    if jogador == 0:
            print('COMPUTADOR VENCEU')
    elif jogador == 1:
            print('EMPATE')
    elif jogador == 2:
            print('JOGADOR VENCEU')
    else:
            print('Jogada Inválida')
elif computador == 2:
    if jogador == 0:
            print('JOGADOR VENCEU')
    elif jogador == 1:
            print('COMPUTADOR VENCEU')
    elif jogador == 2:
            print('EMPATE')
    else:
            print('Jogada Inválida')



