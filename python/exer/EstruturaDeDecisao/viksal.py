#!/usr/bin/python

#Desvio Condicional

#Algoritmo

#Ler numero de um funcionaro
#Numero de horas trabalhada
#Valor que recebe por hora
#Numero de filhos menor de 14 anos
#Salario familia = 5% minimo por filho
#Calcular salario bruto
#Descontar o INSS 8,5% do sal bruto
#Descontar o Imposto de renda

print 'Salario e roubo do governo' #imprimir
print #quebra de linha

id = int(input('Numero do funcionario: ')) #variavel ID = numero do funcionario declara e caputanro valor
mespg = int(input('Numero de horas trabalhadas: ')) #variavel 'mespg' = numero de horas trabalhadas no mes
hrpg = int(input('Pagamento por hora: ')) #variavel hrpg = pagamento por hora
filhos = int(input('quantia de filhos inferior a 14 anos? ')) #variavel filhos = quantidade de filhos com menos de 14 anos

#variaveias globais podendo usar em cada IF
salbruto = mespg * hrpg #variavel salario bruto | salbruto = mespg * hrpg | total do salariobruto
inss = salbruto * 0.085 #variavel inss declarada | inss = salbruto * 0.085 | 0.085 equivale a 8.5% | valor descontado
minf = filhos * 0.05 #variavel minf declarada | minf = filhos * 0.05 | 0.05 = 5% | filhos * 0.05, valor adicionar por filho
print #quebra linha
if salbruto > 1500: #se salbruto for maior que 1500
	ir = salbruto * 0.15 #variavel IR declarada | calculo do imposto de renda quanto descontar
	saliq = minf + salbruto - ir - inss #variavel saliq | salario liquido = minf + salbruto - ir - inss
	print 'Salario liquido: ', saliq #imprimir o salario liquido
	print 'Salario bruto: ', salbruto #imprimir o salario bruto
	print 'Salario por filho (5%): ', minf #imprimir o salario adicional por filho
elif salbruto > 500:
	#variavei locais, podendo usar apenas neste desvio, ate onde comecar o proximo elif
	ir = salbruto * 0.08
	saliq = minf + salbruto - ir - inss
	print 'Salario liquido: ', saliq
	print 'Salario bruto: ', salbruto
	print 'Salario por filho (5%): ', minf
elif salbruto <= 500: #se salbruto <= 500 | declarado apenas o necessario
	print 'Isento do IR:' #imprimir isensao do IR
	saliq = minf + salbruto #variavel saliq = minf + salbruto | total que vai receber
	print
	print 'Salario liquido: ', saliq
	print 'Salario bruto: ', salbruto
	print 'Salario por filho (5%): ', minf
else:
	print


