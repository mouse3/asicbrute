import os
import time
import socketserver
import socket
from uuid import getnode as get_mac
from socket import gethostbyname, gethostname
import random
import string 
from itertools import product
from time import time
from nympy import loadtxt
mac = get_mac()

def bruteforce():
    def product_loop(password, generator):
        for p in generator:
            if ''.join(p) == password:
                print('\nPassword:', ''.join(p))
                return ''.join(p)
        return False


    def bruteforce(password, max_nchar=8):
        """Password brute-force algorithm.
        Parameters
       ----------
        password : string
        To-be-found password.
        max_nchar : int
        Maximum number of characters of password.
        Return
        ------
        bruteforce_password : string
            Brute-forced password
        """
        print('1) Comparing with most common passwords / first names')
        common_pass = loadtxt('probable-v2-top12000.txt', dtype=str)
        common_names = loadtxt('middle-names.txt', dtype=str)
        cp = [c for c in common_pass if c == password]
        cn = [c for c in common_names if c == password]
        cnl = [c.lower() for c in common_names if c.lower() == password]

        if len(cp) == 1:
            print('\nPassword:', cp)
            return cp
        if len(cn) == 1:
            print('\nPassword:', cn)
            return cn
        if len(cnl) == 1:
            print('\nPassword:', cnl)
            return cnl

        print('2) Digits cartesian product')
        for l in range(1, 9):
            generator = product(string.digits, repeat=int(l))
            print("\t..%d digit" % l)
            p = product_loop(password, generator)
            if p is not False:
                return p

        print('3) Digits + ASCII lowercase')
        for l in range(1, max_nchar + 1):
            print("\t..%d char" % l)
            generator = product(string.digits + string.ascii_lowercase,
                            repeat=int(l))
            p = product_loop(password, generator)
            if p is not False:
                return p

        print('4) Digits + ASCII lower / upper + punctuation')
        # If it fails, we start brute-forcing the 'hard' way
        # Same as possible_char = string.printable[:-5]
        all_char = string.digits + string.ascii_letters + string.punctuation

        for l in range(1, max_nchar + 1):
            print("\t..%d char" % l)
            generator = product(all_char, repeat=int(l))
            p = product_loop(password, generator)
            if p is not False:
                return p


    # EXAMPLE
    start = time()
    bruteforce('sunshine') # Try with '123456' or '751345' or 'test2018'
    end = time()
    print('Total time: %.2f seconds' % (end - start))
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
    if option == "bruteforce":
        bruteforce()
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
def inicio():
    menu()
    print(banner)

inicio()