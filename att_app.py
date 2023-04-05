from cryptographyFramework import *
usuario = input("Digite seu usuario: ")
senha = input("Digite sua senha: ")
mensagem1 = ""
mensagem2 = ""
def valida_usuario (usuario):
    while True:
        if len (usuario) > 30:
            usuario = input("O nome do usuario é no máximo 30 caracteres")
        elif usuario[0].islower():
            usuario = input("O nome do usuario deve ter a primeira letra maiuscula")
        elif not usuario.isalnum():
            usuario = input("O nome do usuario não deve ter caracter especial e nem espaço.")
        else:
            return ("O nome do usuario está cadastrado!!")
            
valida_usuario(usuario)

def valida_senha (senha): 
    while True:
        if len (senha) <= 10:
            senha =  input ("A senha deve ter pelo menos 10 caracter")
        elif senha.isalnum():
            senha = input("A senha deve ter um caracter especial")
        elif senha.isalnum():
            senha = input("A senha deve ter um numero")
        elif senha.islower():
            senha = input("A senha necessita ter pelo menos uma letra maiuscula")
        elif senha.islower():
            senha = input("A necessta ter pelo menos uma letra minuscula") 
        else:
            return ("A senha do usuario está cadastrada com sucesso!!")
        
valida_senha(senha)

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

pedirMensagem(mensagem1, mensagem2)
criptar()
printar()

        

