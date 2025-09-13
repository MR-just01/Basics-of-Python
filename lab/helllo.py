# print("hello")
# a=4
# b=6
#AIRTHMETIC OPERATION 
# print(f"the sum of {a} and {b } : " ,a+b)
# print(f"the subraction of {a} and {b} : {a-b}" )
# print(f"the  multiplication of {a} and {b} : {a*b}")
# print(f"the  division of {a} and {b} : {a/b}")
# print(f"the  modulus of {a} and {b} : {a%b}")
# print(f"the power of {a}  : {a**2}")
# print(f"the  float division of {a} and {b} : {a//b}")


#SWAPPING 
# b=a
# a=b
# print(a)
# print(b)

##INPUT THREE NUMBER ND FIND GREATEST OF ALL THREE


# num1 = int(input("enter the number "))
# num2 = int(input("enter the second number "))
# num3 = int(input("enter the third number "))

# if(num1>num2 and num1>num3):
#     print(f"{num1} is greatest among three")
# elif(num2>num1 and num2>num3):
#     print(f"{num2} is the  greatest among three")
# elif(num3>num1 and num3>num2):
#      print(f"{num3} is the  greatest among three")
# else:
#      print(f"{num1}, {num2}, {num3} all are equal")

# import random
# game = ["scissor", "Rock"  , "paper"]
# computer_choice = random.choice(game)

# user_choice = input("Rock , paper or scissor??").lower
# print(computer_choice)
# if(user_choice == computer_choice):
#     print("its a tie")
# elif(user_choice == "rock" and computer_choice=="scissor" or \
#    user_choice == "paper" and computer_choice == "rock" or \
#    user_choice == "scissor" and computer_choice == "paper"):
#     print("congratulations you win!!!")
# elif(user_choice == computer_choice):
#     print("its a tie")
# else:
#     print("opps computer win and you lose ")

 ##number guessing game 
# import random
# c_choice =random.randrange(1,7)
# u_choice = int(input("Enter the number between 1 to 6 :"))
# # print("computer chose : " , c_choice)
# if(u_choice == c_choice):
#     print("you guessed right!!")
# else:
#     print("you guessed wrong")

##dice rolling game

import random 
dice1 = random.randrange(1,7)
dice2 = random.randrange(1,7)

print("first dice has " , dice1 )
print("second has : " ,dice2)

