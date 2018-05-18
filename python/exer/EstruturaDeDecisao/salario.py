#!/usr/bin/python
#as organizacoes resolveram dar um aumento de salario
#programa para recalcular reajuste
#faca um programa que receba o salario de um colaborador
#reajuste segundo o seguinte criterio, baseado no salario atual
#salario ate 280,00: aumento de 20%
#salario entre 280,00 e 700: aumento de 15%
#salario entreo 700,00 e 1500: aumento de 10%
#salarios de 1500 em diante: aumento de 5%

#apos o aumento ser realizado informar na teal
#salario antes do reajuste
#o percentual de aumento aplicado
#o valor do aumento
#o novo salario apos o aumento

print 'Reajuste de salario tabajaras'
print
salario = float(input('Salario atual do colaborador? '))
print
if salario >= 1500:
	sal1 = salario * 0.05
	novo1 = salario + sal1
	print 'Salario antes do reajuste: ', salario
	print 'Aumento de 5% no salario'
	print 'Valor do aumento: ', sal1
	print 'O novo salario: ', novo1
	print
elif salario >= 700:
	sal2 = salario * 0.10
	novo2 = salario + sal2
	print 'Salario antes do reajuste: ', salario
	print 'Aumento de 10% no salario'
	print 'Valor do aumento: ', sal2
	print 'O novo salario: ', novo2
	print
elif salario > 280:
	sal3 = salario * 0.15
	novo3 = salario + sal3
	print 'Salario antes do aumento: ', salario
	print 'Aumento de 15% no salario'
	print 'Valor do aumento: ', sal3
	print 'O novo salario: ', novo3
	print
elif salario <= 280:
	sal4 = salario * 0.20
	novo4 = salario + sal4
	print 'Salario antes do aumento: ', salario
	print 'Aumento de 20% no salario'
	print 'Valor do aumento: ', sal4
	print 'O novo salario: ', novo4
	print
else:
	print
