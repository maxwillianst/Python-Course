from random import shuffle
print('======= Exercício aula 08 =======')
print('======= SORTEIO DE LISTA DE ALUNOS =======')

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A sequência escolhida foi {}'.format(lista))