#!/usr/bin/python
#faca um programa que verifique se a letra digitada
#eh F ou M, conforme
#F - Feminino
#M - Masculino
#Sexo invalido

print 'Sexo do individuo'
print
sexo = raw_input('Insira o sexo: ') #quando se trata de caracteres #raw_input
print
M = 'Masculino'
F = 'Feminino'

if sexo == 'M': #quando se trata de nome, usar '' para string
	print 'Masculino'
elif sexo == 'F':
	print 'Feminino'
else:
	print 'Sexo invalido'
