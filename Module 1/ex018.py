import math
print('======= Exercício aula 08 =======')
print('======= SENO, COSSENO, TANGENTE =======')

ang = float(input('Qual o angulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print ('Se o angulo é {}, o seno é {:.3F}, o cosseno é {:.2F} e a tangente é {:.3F}'.format(ang, sen, cos, tan))