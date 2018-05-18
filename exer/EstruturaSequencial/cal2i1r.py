#!/usr/bin/python
#Faca um programa que peca 2 numeros inteiros
#e 1 numero real e calcule e mostre:
#a. o produto do dobro do primeiro com a metade do segundo
#b. a soma do triplo do primeiro com o terceiro
#c. o terceiro elevao ao cubo

ia = int(input('Primeiro numero inteiro: '))
ib = int(input('Segundo numero inteiro: '))
c = input('Unico numero real: ')

dobrometade = 2 * ia + (ib / 2)
triplosoma = 3 * ia + c
elevado =  c ** 3
print
print 'O produto do dobro do primeiro com metade do segundo: ', dobrometade
print
print 'A soma do triplo do primeiro com o terceiro: ', triplosoma
print
print 'O terceiro elevado ao cubo', elevado
