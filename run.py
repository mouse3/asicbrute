import os
import time
import socketserver
import socket
from uuid import getnode as get_mac
from socket import gethostbyname, gethostname
import random
import string 
from itertools import product
import time
mac = get_mac()

def brutewps():
    os.system("clear")
    os.system("wpspingenerator")
def notbrutewpa():
    print("you need a network card to use this tool")
    time.sleep(2)
    print("downloading...")
    os.system("git clone https://github.com/derv82/wifite2.git")
    os.system("mv wifite2/* .")
    os.system("sudo python setup.py install")
    time.sleep(2)
    os.system("rm setup.py")
    os.system("clear")
    print("running wifite.")
    time.sleep(1)
    os.system("clear")
    print("running wifite..")
    time.sleep(1)
    os.system("clear")
    print("running wifite...")
    time.sleep(2)
    os.system("sudo wifite")
def brutep():
    print("en creacion")
def info():
    nombre_equipo = socket.gethostname()
    iplocal = socket.getsockname()
    direccion_equipo = socket.gethostbyname(nombre_equipo)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print(s.getsockname()[0])
    print(mac)
    print(direccion_equipo)
    print(nombre_equipo)
    print(iplocal)
def LHOST():
    ip = "0.0.0.0"
    puerto = 9966
    d = (ip, puerto)
    conexionesMaximas = 500
    servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    servidor.bind(d) #Asignamos los valores del servidor
    servidor.listen(conexionesMaximas) #Asignamos el número máximo de conexiones
    
    print("Esperando conexiones en %s:%s" %(ip, puerto))
    cliente, direccion = servidor.accept()
    print("Conexion establecida con %s:%s" %(direccion[0], direccion[1]))

#Bucle de escucha. En él indicamos la forma de actuar al recibir las tramas del cliente
    while True:
        datos = cliente.recv(1024)
        if datos == "exit":
            cliente.send("exit")
            break
        if datos == "running":
            print("Recibido: %s" %datos)
            cliente.sendall("me too")
            continue
        print("RECIBIDO: %s" %datos)
        cliente.sendall("-- Recibido --")

    print("------- CONEXIÓN CERRADA ---------")
    servidor.close()
def Connect():
    ipServidor = "0.0.0.0" 
    puertoServidor = 9966
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((ipServidor, puertoServidor))
    print("Conectado con el servidor ---> %s:%s" %(ipServidor, puertoServidor))

    print("------- CONEXIÓN CERRADA ---------")
    cliente.close()
bruteh = """
#################################################################
#   -wps bruteforce wps                                         #
#   -wpa bruteforce wpa                                         #
#   -p bruteforce at a password                                 #
#   -gmail bruteforce at an account from gmail                  #
#                                                               #
#                                                               #
#                                                               #
#################################################################
           """
comandos = """
#################################################################
#   -help how to use                                            #
#   -lhost create a localserver                                 #
#   -connect connect to the LHOST                               #
#   -bruteforce set the menu for a bruteforce                   #
#                                                               #
#                                                               #
#                                                               #
#################################################################
           """
banner = """
#############################
#   Welcome to HashBrute    #
#                           #
#type help for command help#
#                           #
#############################
         """
print(banner)
print(mac)
def menu():
    option = input(">>>")
    if option == "brutefoce-wps":
        brutewps()
    if option == "pbruteforce-wpa":
        brutewpa()
    if option == "bruteforce -p":
        brutep()
    if option == "data":
        info()
    if option == "lhost":
        LHOST()
    if option == "connect":
        Connect()
    if option == "commands":
        print(comandos)
        time.sleep(10)
        inicio()
    if option == "help":
        print("Run ASIC.py on the ASIC hash")
        print("if you don't have the ASIC buy it on www.ASICbrute.com")
        print("")
        print("create a pythonserver with the comand LHOST")
        print("stay on listen in the server Lhost")
        print("connect the ASIC on the server")
        time.sleep(5)
        inicio()
    if option == "bruteforce -h":
        print(bruteh)
def inicio():
    menu()
    print(banner)

inicio()
