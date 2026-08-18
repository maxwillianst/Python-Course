print('======= Exercício aula 12 =======')
print('======= Simulador de empréstimo =======')

valorcasa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos deseja pagar? '))
prestacao = valorcasa / (anos * 12)
limite = salario * 30 / 100
if prestacao <= limite:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo reprovado!')

