#!/usr/bin/python
#tendo como dado de entrada a altura de uma pessoa
#construa um algoritmo que calcule seu peso ideal
#utilizando as seguintes forumas:
#para homens (72.7*h) - 58
#para mulheres (62.1*h) - 44.7

print 'Peso ideal para ambos sexos'
print
h = float(input('Qual a altura do individuo? '))
FH = 72.7 * h - 58
FF = 62.1 * h - 44.77
print
print 'O peso ideal para esta altura masculino: ', FH
print
print 'O peso ideal para esta altura feminino: ', FF
