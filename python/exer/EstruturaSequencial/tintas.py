#!/usr/bin/python
#O programa devera pedir o tamanho em metros quadrados da area a ser pintada
#considere que a cobertura da tinta e de 1L para cada 3 metros quadrados
#e que a tinta vendida em latas de 18L que custam R$80,00
#informe a quantidade de latas de tinta a serem compradas e o preco total

print 'Loja de tintas virtual'
print
metros = int(input('metros quadrados: '))
litro = metros / 3
latas = float(metros / 18)
valor =  float(latas * 80.00)

print
print 'Total de latas de tintas: ', latas
print
print 'Total em valor: ', valor
