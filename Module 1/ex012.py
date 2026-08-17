print('======= Exercício aula 07 =======')
print('======= CALCULO DE DESCONTO =======')

preco = float(input('Qual o preço do produto? '))
desconto = float(input('Quantos % de desconto o produto tem? '))
novoValor = preco - (preco * desconto/100)
print('Valor do desconto: R$ {:.2f} \nPreço do produto com desconto: {} '.format(desconto, novoValor))