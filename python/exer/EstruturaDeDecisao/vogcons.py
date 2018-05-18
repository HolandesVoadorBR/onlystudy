#!/usr/bin/python
#faca um programa que verifique se
#uma letra digitada eh vogal ou
#consoante

print 'Verificador de consoantes e vogais'
print
letra = raw_input('Inserir letra: ')
print

vogais = ['a', 'e', 'i', 'o', 'u'] #criamos a lista das vogais

if letra not in vogais: #se variavel letra nao estiver em vogais
	print 'Consoante' #Consoante
else: #Senao
	print 'Vogal' #Vogal
