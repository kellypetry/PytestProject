from validas import * 

def test_valida_usuario():
    assert valida_usuario ("kelly") == False 
    assert valida_usuario ("Kellyyyyyyyyyyyyyyyyyyyyyyyyyyy") == False
    assert valida_usuario ("Kelly_") == False
    assert valida_usuario ("Kelly") == True
def test_valida_senha():
    assert valida_senha ("kelly123") == False
    assert valida_senha ("kelly7") == False 
    assert valida_senha ("Kelly") == False
    assert valida_senha ("kelly") == False
    assert valida_senha ("kelly_") == False
    assert valida_senha ("Kelly123456789_") == True
    

