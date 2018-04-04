import socket
import sys

def menu():
    print ("\n-------------------------MENU-----------------------")
    print(" W : Ileri")
    print(" A : Sol")
    print(" S : Geri")
    print(" D : Sag")
    print ("------------------------------------------------")

def getCommand():   
    komut = raw_input("Komut Girin(W,A,S,D): ")
    if (komut != "W" and komut != "w" and  komut != "A" and komut != "a" and komut != "S" and komut != "s" and komut != "D" and komut != "d"):
        print("Command did not find!")
        return "null"
    return komut

def forward(connection):
    connection.send("W")
    print >> sys.stdout, 'Sent data  to the client'
def left(connection):
    connection.send("A")
    print >> sys.stdout, 'sent data  to the client'
def right(connection):
    connection.send("D")
    print >> sys.stdout, 'Sent data  to the client'
def backward(connection):
    connection.send("S")
    print >> sys.stdout, 'Sent data  to the client'