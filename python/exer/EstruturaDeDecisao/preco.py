#!/usr/bin/python
#faca um programa que pergunte o preco de tres produtos
#e informe qual o produto voce deve comprar, sabendo que
#a decisao e sempre pelo mais barato

print 'Menor preco'
print
produts = 3
valor = []

for n in range(0,int(produts)):
	valor.append(int(input('Valor da pasta mais barata? ')))
print
print 'O valor da pasta mais barata: ', min(valor)
print
print 'O valor da pasta mais cara: ', max(valor)
print
print 'Recomenda se comprar a pasta mais barata: ', min(valor)
print
