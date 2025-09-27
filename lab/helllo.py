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
# print("computer chose : " , c_choice)
# # attempt = 3
# # # while(attempt>0):
# if(u_choice >c_choice):
#     print("you guessed the higher number!!")
# elif(u_choice == c_choice):
#     print("you guessed right !!")
# else:
#      print("you guessed wrong number ")
    
# ##dice rolling game

# # import random 
# # dice1 = random.randrange(1,7)
# # dice2 = random.randrange(1,7)

# # print("first dice has " , dice1 )
# # print("second has : " ,dice2)

# print("welcome to the two dice rolling ")

# import math
# base = int(input("enter the base of the triangle "))
# height = int(input("enter the height of the triangle "))
# hypotenus = math.sqrt(base**2 + height**2)
# print("the hypotenus of the triangle is : " , hypotenus)

# for i in range(1,11,2): ## here the last 2 is the sequence in which we are printing 
#     print(i)
# for i in range (5,55 , 5):
#     print(i)
 
# ##insertion sort in python
# array = [12, 155, 10,9,3,5]
# print("array before sorting : " ,array) 
# for i in range(1,len(array)):
#     key = array[i]
#     j=i-1
#     while j>=0 and array[j]>key:
#         array[j+1] = array[j]
#         j-=1
#         array[j+1] = key

# print("array after sorting : " ,array)

# ##selection sort 
array = [12, 155, 10,9,3,5]
print("array before sorting : " ,array)
for i in range(len(array)):
    min = i
    for j in range(i+1 , len(array)):
        if array[j]<array[min]:
            min = j

    array[i],array[min] = array[min],array[i] #swapping withour using the third variable 

  

print("array after sorting : " ,array)