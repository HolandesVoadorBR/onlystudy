#!/usr/bin/python
#faca um programa que leia tres numeros
#e mostre o maior deles

print 'Mostrar o maior entre os 3 numeros'
print
abc = 3 #quantidade de numeros = 3
numeros = [] #declaramos a lista limpa
for n in range(0,int(abc)): #para n em distancia 0, numeros inteiros em variavel abc
	numeros.append(int(input('Digite o numero: '))) #numeros salvos na lista
print 'Maior numero da lista: ', min(numeros) #numero maximo dentro da lista


