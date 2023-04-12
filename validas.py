def valida_usuario(usuario):
    if len (usuario) > 30:
        print("O nome do usuario é no máximo 30 caracteres")
        return False 
    elif usuario[0].islower():
        print("O nome do usuario deve ter a primeira letra maiuscula")
        return False
    elif not usuario.isalnum():
        print("O nome do usuario não deve ter caracter especial e nem espaço.")
        return False
    else:
        print ("Usuario certo!!")
        return True
    
def valida_senha (senha): 
    if len (senha) <= 10:
            print("A senha deve ter pelo menos 10 caracter")
            return False 
    elif senha.isalnum():
            print("A senha deve ter um caracter especial")
            return False 
    elif senha.isalnum():
            print("A senha deve ter um numero")
            return False
    elif senha.islower():
            print("A senha necessita ter pelo menos uma letra maiuscula")
            return False
    elif senha.islower():
            print("A necessta ter pelo menos uma letra minuscula") 
            return False
    else:
        print("Senha correta!!")
        return True