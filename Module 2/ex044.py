print('======= Exercício aula 12 =======')
print('======= Valor a ser pago =======')

produto = float(input('Qual o valor do produto? '))
pagamento = float(input('Como deseja pagar?\n1-À vista dinhero/cheque: 10% de desconto.\n2-À vista no cartão: 5% de desconto.\n3-Em até 2x no cartão: preço normal.\n4-3x ou mais no cartão: 20% de juros.\nDigite a sua opção:'))
op1 = produto - (produto * 0.10)
op2 = produto - (produto * 0.05)
op3 = produto / 2
op4 = produto + (produto * 0.20)
if pagamento == 1:
    print(f'O produto com o desconto de 10% fica {op1}')
elif pagamento == 2:
    print(f'O produto com o desconto de 5% fica {op2}')
elif pagamento == 3:
    print(f'Em até 2x o produto não terá juros e a primeira parcela será de {op3}')
elif pagamento == 4:
    print(f'O produto com 20% de juros fica R${op4:.2f}')