# author: Daniel Terreros

# description: A password program.

sPassword = input( "Please enter a password that is at least 8 characters: ")
while len(sPassword) < 8 :
    print( "The password needs to be at least 8 characters. Please try again. ")
    sPassword = input( "Please enter a password that is at least 8 characters: ")