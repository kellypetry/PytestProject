from cryptographyFramework import *

initializeWrite()
user = "Kelly"
password = "perola2020"
encryptedText = encryptMessage(user, password, "Sexta vai começar o inglês!!!")
saveNewLine(encryptedText)
encryptedText = encryptMessage(user, password, "Estou ansiosa!!!")
saveNewLine(encryptedText)

