#!/usr/bin/python
#faca um programa que leia tres numeros
#e mostre-os em ordem decrescente

print 'Numeros em ordem decrescente'
print
tres = 3 #quantidade pre definida
ordem = [] #declarando lista

for n in range(0, int(tres)): #somente interiso em variavel tres
	ordem.append(input('Quais os numeros: ')) #incluimos na lista os numeros
print 'Ordenada maior ao menor: ', sorted(ordem, reverse=True) #sortiamos eles em ordem reversa verdadeiro
