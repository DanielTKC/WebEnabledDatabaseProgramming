# author: Daniel Terreros

# description: A password program.

sPassword = input( "Please enter a password that is at least 8 characters: ")
while len(sPassword) < 8 :
    print( "The password needs to be at least 8 characters. Please try again. ")
    sPassword = input( "Please enter a password that is at least 8 characters: ")


def buildABetterPassword(sPassword):
    sPassword = sPassword.replace("e", "3")
    sPassword = sPassword.replace("E", "3")
    sPassword = sPassword.replace("i", "7")
    sPassword = sPassword.replace("I", "7")
    sPassword = sPassword.replace("l", "1")
    sPassword = sPassword.replace("L", "1")
    sPassword = sPassword.replace("o", "0")
    sPassword = sPassword.replace("O", "0")
    sPassword = sPassword.replace("p", "9")
    sPassword = sPassword.replace("P", "9")
    sPassword = sPassword.replace("s", "$")
    sPassword = sPassword.replace("S", "$")
    sPassword = sPassword.replace("1", "!")
    sPassword = sPassword.replace(" ", "_")