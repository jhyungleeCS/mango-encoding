import random
import sys
#from re import A
import string
import base64
##Test comment
#Loop to Create Password
while True:
    password_length = int(input('How many characters would you like your password to be?: '))
    password = ""

    for var in range(0, password_length):
        #Added only letters in order to try to use multiple encryption styles
        #pr = random.choice(string.ascii_uppercase + string.ascii_lowercase)
        #Added numbers to try with numbers but currently not understanding how to shift numbers. 
        pr = random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
        password = password + pr   
    print('Generated Password: ' + password)
    break

encryption_pr = input('Do you want an Encoded version of your password?(y/n): ')
#Encryption Base64 Functions 
def encrypt_base64():
    base64_string = password
    base64_bytes = base64_string.encode("utf-8")
    base64_encoded_password = base64.b64encode(base64_bytes)
    print("Your Base64 Encoded Password: ", base64_encoded_password)

#Encryption Caesar Cipher Function
#def caesar_cipher():
#    shift = 3
#    encryption = ""
#    for c in password:
#        if c.isupper():
#            c_unicode = ord(c)
#            c_index = ord(c) - ord("A")
#            new_index = (c_index + shift) % 26
#            new_unicode = new_index + ord("A")
#            new_character = chr(new_unicode)
#            encryption = encryption + new_character
#        else: 
#            encryption += c 
#    print("Your Caesar Cipher Encryption Password: ", encryption)

#Encryption Loop
while True:
    for retry in range(3):
        if encryption_pr == "Yes" or encryption_pr == "yes" or encryption_pr == "Y" or encryption_pr == "y":
            print( 
            "[1] Base64 \n"
            "[2] Base32 \n"
            "[3] Base16 \n"
            "[4] Citrix CTX1 \n"
            "[5] Octal \n"
            "[6] Hex \n"
            "Choose an Encoding Format from above (#): ")
            choice = input('')    
            if choice == "1":
                encrypt_base64()
                break
            
            else: 
                print("Format Not Valid! \n")
                print("============================")
                print("\n")
                break
        elif encryption_pr == "No" or encryption_pr == "no" or encryption_pr == "N" or encryption_pr == "n":
            print("Good-bye! \n" + "Remember your password: " + password)
            break
        else:
            print("Yes or No only")
            break
    else:
        print("Number of attempts exceeded...")
        sys.exit(1)
    break
