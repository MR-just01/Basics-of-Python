# CODEx QUESTIONS OF PYTHON


import math

num1 = int(input("Enter the number(a):  "))
num2 = int(input("Enter the number(b): "))
c= math.sqrt(num1**2 + num2**2)

print(f"hypotenuse is : {c}" )


pesos = float(input("What do you have left in pesos?"))
soles = float(input("What do you have left in soles?"))
reais = float(input("What do you have left in reais? "))

usd1 = pesos/18
usd2 = soles/3.7
usd3 = reais/5.2

total_usd = usd1+usd2+usd3

print(f"total usd: {total_usd}")



import random

num = random.randint(0, 1)   # Generates a random number that's either 0 or 1

if num > 0.5:
  print('Heads')
else:
  print('Tails')


# Write code below 💖
grade = float(input("Enter your marks between 1-100 : "))
if(grade>=55):
  print("you passed")
else:
  print("you failed")

import random
# question  = input("is this line is straight? : ")
answer = ['no ','yes' , 'maya be' ,'i have no idea' , 'i like guys', "Yes, definitely.",
    "No, not at all.",
    "Maybe... who knows?",
    "Absolutely!",
    "I don't think so.",
    "Yes, but be careful.",
    "No, and you know why.",
    "Could be true.",
    "Signs point to yes."] 

response = (random.choice(answer))

print("is this line straight ?? :  " , response)


# They're now installing a new entry system (the height requirement is 137 cm and the cost is 10 credits) and need your help writing the program for it!

# Create a new file called the_cyclone.py.

# Ask the user what their height is and how many credits they have, and store the values in a height variable and a credits variable.

# Use a combination of relational and logical operators to create the rules:

# If they are tall enough and have enough credits, print "Enjoy the ride!"
# Else if they have enough credits, but they aren't tall enough, print "You are not tall enough to ride."
# Else if they are tall enough, but they don't have enough credits, print "You don't have enough credits."
# Else, print a message saying they have not met either requirement.


height = float(input("Enter your height in the cms : "))
credits = float(input("How many credits do you have ???"))

if(height >= 137 and credits >=10):
    print("Enjoy the ride!")
elif(height<137 or credits == 10 ):
    print("You are not tall enough to ride.")
elif(height == 137 or credits< 10):
    print("You don't have enough credits.")
else:
    print("you don't met either requirement.")



Gryffindor =0
Ravenclaw = 0
Hufflepuff =0 
Slytherin = 0 

print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")

answer = int(input("Enter your answer : "))
if(answer == 1):
  Gryffindor +=1
elif(answer == 2):
  Ravenclaw +=1
else:
  print("wrong input")

print("Q2) When I’m dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")
 
answer2 = int(input("enter your ans: " ))
if(answer2 == 1):
  Hufflepuff += 2
elif(answer2 ==2):
  Slytherin += 2
elif(answer2 ==3):
  Ravenclaw += 2
elif(answer2 ==4):
   Gryffindor += 2
else:
  print("Wrong output")

print(" Which kind of instrument most pleases your ear?")
print("1)The violin ")
print("2)The trumpet")
print("3)The piano")
print("4)The drum ")
 
answer3 = int(input("enter your ans: " ))
if(answer3 == 1):

  Slytherin += 4
elif(answer3 ==2):
  Hufflepuff +4
elif(answer3 ==3):
  Ravenclaw += 4
elif(answer2 ==4):
   Gryffindor += 4
else:
  print("Wrong output")

print("score of the Gryffindor :  " ,Gryffindor)  
print("score of the Ravenclaw : " ,Ravenclaw)
print("score of the ufflepuff : ",Hufflepuff)
print("score of the Gryffindor : " ,Gryffindor )


