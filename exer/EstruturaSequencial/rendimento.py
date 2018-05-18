#!/usr/bin/python
#Controlar rendimento diario de seu trabalho
#Toda vez que ele traz um peso de peixes maior que
#o estabelecido pelo regulamento de pesca(50 quilos)
#deve pagar uma multa de R$4,00 por quilo exdecente
#Programa que leia variavel peso
#(peso de peixes) e calcule o excesso
#Gravar na variavel excesso a quantidade de quilos alem do limite
#e na variavel multa o valor da multa que joao devera pagar

print 'Calculador de multas e pesos para joao'
print
kg = int(input('Quantos quilos trouxe? ')) #pega os kilos
excesso = kg - 50 #calculo o excesso
print #quebra a linha

if excesso >= 1: #se excesso for maior ou igual a 1, calcula a multa
	multa = 4 * excesso
	print 'Deve pagar: ', multa
else:
	print 'Tudo em ordem'

