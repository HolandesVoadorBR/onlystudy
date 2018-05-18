#!/usr/bin/python

#Faca um programa que peca o tamanho de um arquivo para download em MB
#A velocidade da internet em MBPSe calcule e informe o tempo
#aproximado do download do arquivo usando esse link em minutos

print 'calculador de download'
print
arquivo = int(input('Tamanho do arquivo em MB? '))
print
internet = int(input('Tamanho da internet em Mbps?' ))
print
tempo = arquivo / internet
seg = 60*1
minutos = tempo / seg
print 'Tempo total para demora em minutos: ', minutos
