#!/usr/bin/python
#Ler duas notas obtidas por um aluno
#obtidas por um aluno ao longo do semestre
#calcule sua media, atr conc. tab abaixo
#media de aproveitamento conceito
#entre 9 e 10 A
#entre 7.5 e 9 B
#entre 6 e 7.5 C
#entre 4.0 e 6.0 D
#entre 4 e zero E
#Deve mostrar na tela
#as notas, a media, o conceito correspondete e a mensagem
#Aprovado para A, B, C
#Reprovado para D ou E

print 'Aproveitamento'
print
prova1 = float(input('Nota da prova 1: ')) #pegar valor pr1
prova2 = float(input('Nota da prova 2: ')) #pegar valor pr2
media = (prova1 + prova2)/2 #calcular media
print
if media >= 9.0: #se
	print 'Nota prova 1: %d | Nota prova 2: %d ' % (prova1, prova2) #chamar variaveis
	print 'A Media foi: %d | Conceito: A ' % (media) #chamar media
	print 'Aprovado' #imprimir
elif media >= 7.5:
	print 'Nota prova 1: %d | Nota prova 2: %d ' % (prova1, prova2)
	print 'A media foi: %d | Conceito: B' % (media)
	print 'Aprovado'
elif media >= 6.0:
	print 'Nota prova 1: %d | Nota prova 2: %d ' % (prova1, prova2)
	print 'A media foi: %d | Conceito: C' % (media)
	print 'Apovado'
elif media >= 4.0:
	print 'Nota prova 1: %d | Nota prova 2: %d ' % (prova1, prova2)
	print 'A media foi: %d | Conceito: D' % (media)
	print 'Reprovado'
else:
	print 'Nota prova 1: %d | Nota prova 2: %d ' % (prova1, prova2)
	print 'A media foi %d | COnceito: E' % (media)
	print 'Reprovado'
