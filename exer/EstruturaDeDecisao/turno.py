#!/usr/bin/python
#faca um programa que pergunte em que turno voce estuda
#peca para digitar M-matutino, V-vespertino ou N-noturno
#imprima a mensagem
#Bom dia
#Boa tarde
#Boa noite
#Valor invalido, conforme o caso

print 'Turnos'
print
print 'M para matutino'
print 'V para vespertino'
print 'N para noturno'
print
turno = raw_input('Qual turno voce estuda? ') #declaramos e pegamos o valor de character
print
if turno == 'M': #se for igual a M
	print 'Bom dia' #imprimi
elif turno == 'V': #senao se for igual a V
	print 'Boa tarde' #imprimi
elif turno == 'N': #senao se for igual a N
	print 'Boa noite' #imprimi
else: #Senao
	print 'Valor invalido' #imprimi
