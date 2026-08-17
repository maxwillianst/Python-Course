print('======= Exercício aula 09 =======')
print('======= LEITOR DE fRASE =======')

frase = str(input('Digite uma frase: ')).lower().strip()
print('A letra (a) aparece {} vezes'.format(frase.count('a')))
print('A letra (a) aparece primeiro na posição {}'.format(frase.find('a')+1))
print('A letra (a) aparece por último na posição {}'.format(frase.rfind('a')+1))


