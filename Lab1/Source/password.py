import re
pw= input("Input your password : ")
temp = True
while temp:
    if (len(pw)<6 or len(pw)>16):
        break
    elif not re.search("[0-9]",pw):
        break
    elif not re.search("[$@!*]",pw):
        break
    elif not re.search("[a-z]",pw):
        break
    elif not re.search("[A-Z]",pw):
        break
    else:
        print("Valid Password")
        temp=False
        break

if temp:
    print("Not a Valid Password")