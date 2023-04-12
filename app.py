from cryptographyFramework import *
from validas import *
usuario = ""
senha = ""
mensagem1 = ""
mensagem2 = ""
def solicita_ususario ():
    while True:
        usuario = input(" Digite seu usuario: ")
        if valida_usuario(usuario):
            break

def solicita_senha (): 
    while True:
        senha = input("Digite sua senha: ")
        if valida_senha (senha):
            break

def pedirMensagem (mensagem1, mensagem2):
    mensagem1 = input ("Digite sua primeira mensagem: ")
    mensagem2 = input ("Digite sua segunda mensagem: ")
    print ("Aleatoria")
def criptar():
    initializeWrite()
    encryptedText = encryptMessage(usuario, senha, mensagem1)
    saveNewLine(encryptedText)
    encryptedText = encryptMessage(usuario, senha, mensagem2)
    saveNewLine(encryptedText)
def printar():
    initializeRead()
    line1 = readNextLine()
    print(line1)
    print(decryptMessage(usuario, senha, line1))
    line2 = readNextLine()
    print(line2)
    print(decryptMessage(usuario, senha, line2))

solicita_ususario()
solicita_senha()
pedirMensagem(mensagem1, mensagem2)
criptar()
printar()