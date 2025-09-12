#1. Write a python program to display a user entered name followed by Good
#      #Afternoon using input () function.
# name = input("Enter your name ")
# print(f"good morning {name} ♥️♥️")

##Write a program to fill in a letter template
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>" , "Maya").replace("<|Date|>" ,"20-04-2025"))

#Write a program to detect double space in a string.
name = "Lion is the king   of the jungle "
print(name.find("  "))

## write the program to replace the third from the double space to single space 
name  = " how does that matter to you   "
print(name.replace("   " , " "))

##write a program to formate the following using the escape sequence character
letter = "Dear maya,\n\t This pyhton course is fine .. \nThanks !!"
print(letter)
