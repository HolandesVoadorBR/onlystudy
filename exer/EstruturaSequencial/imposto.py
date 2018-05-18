#!/usr/bin/python
#faca um programa que pergunte quanto ganha por hora
#e o numero de hora trabalha no mes
#calcule e mostre o total do salario descontar os impostos
#11% imposto de renda
#8% INSS
#5% sindicato
#fazer um programa que de:
#a. salario bruto
#b. quanto pagou ao INSS
#c. quanto pagou ao sindicato
#d. o salario liquido
#e. calcule os descontos e o salario liquido

print 'Calculador de salario'
print
pghr = int(input('Quanto ganha por hora? '))
mes = int(input('Horas que trabalhou no mes? '))

total = pghr * mes
renda = total * 0.11
inss = total * 0.08
sindicato = total * 0.05
liquido = total - renda - inss - sindicato

print
print 'Salario bruto total: ', total
print
print 'Total pago para o imposto de renda: ', renda
print
print 'Total pago para o INSS: ', inss
print
print 'Total pago para o sindicato: ', sindicato
print
print 'Salario liquido: ', liquido
