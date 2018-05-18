#!/usr/bin/python
#faca um programa para leitura de duas notas parciais
#O programa deve calcular a media alcancada por aluno
#A mensagem Aprovado se media > 7
#A mensagem Reprovada se media < 7
#A mensagem Aprovado com distincao se media == 10

print 'Aprova alunos'
print
nota1 = int(input('Primeira nota: '))
nota2 = int(input('Segunda nota: '))
media = (nota1 + nota2)/2
print
if  media > 9: #se a media > 9 ou seja 10, 11
	print 'Aprovado com distincao' #imprimi
elif media >= 7: #se a media >= 7 ou seja 7, 8, 9 e < 10
	print 'Aprovado' #imprimi
else:
	print 'Reprovado' #se a media < 7 ou seja 6, 5, 4
