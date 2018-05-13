#!/usr/bin/python

#cliente faz a connection e necessario uso do netcat para poder interagir e ouvir as portas
import socket

target = "127.0.0.1" #alvo
port = 445 #porta

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Conexao TCP

client.connect((target,port)) #faz a connection e chama as variaveis

client.send("Try") #se conectar ele envia um "Try" / usar netcat

response = client.recv(4096) #resposta
print response
