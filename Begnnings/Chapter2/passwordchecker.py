## min 8 character ,digits , uppercase, lowercase and special character

import re 

def check_strengh(password):
    if len(password)<8:
        return "weak : password must be at least 8 character"
    if not any(char.isdigit() for char in password):
        return "weak : password must contain a digit"
    if not any(char.isupper() for char in password):
        return "weak : password must contain a capitla letter"
    if not any(char.islower() for char in password):
        return "weak : password must contain a small letter"
    if not re.search(r'[!@#$%^&*() {} <> , ?] ' , password):
        return "Medium: password must contain a special character"

    return " Strong: password is secure"      

def password_Checker():
    print("welcome to the password strength checker")
     
    while True:
        password = input("Enter your password  / type 'exit ' to quit : ")

        if(password.lower  == exit):
            print("Thankyou for using our Tool!!! ")
            print("Exiting you out")
            break
        else : 
          result  =  check_strengh(password)
          print(result)

    
##RUN THE PASSWORD CHECKER TOO
if __name__ == "__main__":
    password_Checker()