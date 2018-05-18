#!/usr/bin/python
#faca um programa calculo de uma folha de pagamento
#descontos do imposto de renda
#depende do salario bruto
#e 3% do sindicato
#o fgts corresponde ao 11% do salario bruto
#salario liquido corresponde ao salario bruto menos os descontos
#o programa devera pedir ao usuario o valor da sua hora e qt hrs no mes
#Descontos Imposto de Renda
#Salario bruto ate 900 - isento
#Salario bruto ate 1500 - 5%
#Salario bruto ate 2500 - 10%
#Salario bruto acima de 2500 - 20%
print 'Roubo do governo'
print
salhr = int(input('Salario hora: '))
hrmes = int(input('Horas trabalhas no mes: '))
salbruto = salhr * hrmes

sindicato = salbruto * 0.03
fgts = salbruto * 0.11

print

if salbruto > 2500:
	ins1 = salbruto * 0.20
	det1 = sindicato + fgts + ins1
	liq1 = salbruto - det1
	print 'Salario bruto: ', salbruto
	print 'Sindicato (3%): ', sindicato
	print 'INSS (20%): ', ins1
	print 'FGTS (11%): ', fgts
	print 'Total de descontos: ', det1
	print 'Salario liquido: ', liq1
elif salbruto >= 1500:
	ins2 = salbruto * 0.10
	det2 = sindicato + fgts + ins2
	liq2 = salbruto - det2
	print 'Salario bruto: ', salbruto
	print 'Sindicato (3%): ', sindicato
	print 'INSS (10%): ', ins2
	print 'FGTS (11%): ', fgts
	print 'Total de descontos: ', det2
	print 'Salario liquido: ', liq2
elif salbruto >= 900:
	ins3 = salbruto * 0.05
	det3 = sindicato + fgts + ins3
	liq3 = salbruto - det3
	print 'Salario bruto: ', salbruto
	print 'Sindicato (3%): ', sindicato
	print 'INSS (5%): ', ins3
	print 'FGTS (11%): ', fgts
	print 'Total de descontos: ', det3
	print 'Salario liquido: ', liq3
elif salbruto > 0:
	det4 = sindicato + fgts
	liq4 = salbruto - det4
	print 'Salario bruto: ', salbruto
	print 'Sindicato (3%): ', sindicato
	print 'INSS(0%): isento'
	print 'FGTS (11%): ', fgts
	print 'Total de descontos: ', det4
	print 'Salario liquido: ', liq4
else:
	print
