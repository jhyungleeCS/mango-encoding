from ast import Return
import random
import sys
#from re import A
import string
import base64

password_length = input("How many characters would you like your password to be?: ")
password = ""

while password_length.digit():
    continue
else: 
    password_length = input("Number value only! : \n")
for var in range(0, password_length):
        pr = random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
        password = password + pr   
        print('Generated Password: ' + password)


#Loop to Create Password
#while True:
#    password_length = int(input('How many characters would you like your password to be?: '))
#    password = ""
#    while password_length.digit() == "True":
#        continue
#    else:
#        password_length = int(input("Valid Number Only! : \n"))
#    for var in range(0, password_length):
#        pr = random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
#        password = password + pr   
#    print('Generated Password: ' + password)
#    break

encryption_pr = input('Do you want an Encoded version of your password?(y/n): ')
###########################################################################   
#Encoding Base64 Function
def encode_base64():
    base64_string = password
    base64_bytes = base64_string.encode("utf-8")
    base64_encoded_password = base64.b64encode(base64_bytes)
    print("Your Base64 Encoded Password: ", base64_encoded_password)
###########################################################################   
#Encoding Base32 Function
def encode_base32():
    base32_string = password 
    base32_bytes = base32_string.encode("utf-8")
    base32_encoded_password = base64.b32encode(base32_bytes)
    print("Your Base32 Encoded Password: ", base32_encoded_password)
###########################################################################
#Encoding Base16 Function
def encode_base16():
    base16_string = password
    base16_bytes = base16_string.encode("utf-8")
    base16_encoded_password = base64.b16encode(base16_bytes)
    print("Your Base16 Encoded Password: ", base16_encoded_password)
###########################################################################    

  
#Encoding Loop
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
            "Choose an Encoding Format from Above (#): ")
            choice = input('')    
            if choice == "1":
                encode_base64()
                break
            elif choice == "2": 
                encode_base32()
                break
            elif choice == "3":
                encode_base16()
                break
            else: 
                print("!!! Format Not Valid !!! \n")
                #print("Choose an Encoding Format from Below: \n")               
        elif encryption_pr == "No" or encryption_pr == "no" or encryption_pr == "N" or encryption_pr == "n":
            print("Good-bye! \n" + "Remember your password: " + password)
            break
        else:
            encryption_pr = (input("Yes or No Only: \n"))
    else:
        print("Number of attempts exceeded...")
        sys.exit(1)
    break
