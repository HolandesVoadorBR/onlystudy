#!/usr/bin/python
#O programa devera pedir o tamanho em metros quadrados da area a ser pintada
#considere que a cobertura da tinta e de 1L para cada 6 metros quadrados
#e que a tinta vendida em latas de 18L que custam R$80,00
#ou em galoes de 3,6 litros que custam R$25,00
#informe ao usuario a quantidade de tinta a serem compradas
#e os respectivos precos em 3 situacoes
#comprar apenas latas de 18 litros
#comprar apenas galoes de 3,6 litros
#misturar latas e galoes de forma que o preco seja o menor
#acrescente 10% de folga e sempre arredonde os valores para cima
#isto e, considere as latas cheias

print 'Loja de tintas virtual'
print
metro = int(input('Metragem da sala? '))
print

cobertura = metro / 6
tinta = float(metro / 18)
valor = float(tinta*80.00)

galoes = float(metro / 3.6)
galoesval = float(galoes*25.00)

print 'A quantidade de latas de tintas a serem compradas: ', tinta
print
print 'A quantidade de galoes a semrem comprados: ', galoes
print
print 'Comprar apenas latas de 18L: ', valor
print
print 'Comprar apenas galoes de 3.6L: ', galoesval

# Faltou acrescentar os 10% e misturar galoes e tintas preco menor
