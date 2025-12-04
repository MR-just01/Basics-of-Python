#          #ROCK PAPER SCISSOR GAME 

# import random

# game = ["rock", "paper", "scissor"]
# max_attempts = 3
# attempt = 0

# while attempt < max_attempts:
#     user_choice = input("Rock, paper, or scissor? ").lower()
    
#     if user_choice not in game:
#         print("Invalid choice, try again.\n")
#         continue
    
#     computer_choice = random.choice(game)
#     print(f"Computer chose: {computer_choice}")
    
#     if user_choice == computer_choice:
#         print("It's a tie!")
#     elif (user_choice == "rock" and computer_choice == "scissor") or \
#          (user_choice == "paper" and computer_choice == "rock") or \
#          (user_choice == "scissor" and computer_choice == "paper"):
#         print("Congratulations, you win!!!")
#     else:
#         print("Oops, computer wins and you lose!")
    
#     attempt += 1
#     print(f"Attempt {attempt} of {max_attempts}\n")

# print("Game over!")


# NUMBER GUESSING GAME


# import random
# c_choice =random.randrange(1,7)

# print("computer chose : " , c_choice)
# attempt = 0 
# max_attempt = 3
# while(attempt<max_attempt):
#     u_choice = int(input(f" Attempt {attempt+1} : Enter the number between 1 to 6 :"))
#     attempt+=1
#     if(u_choice == c_choice):
#      print("you guessed the right number!!")
#     elif(u_choice > c_choice):
#      print("you guessed  higher number !!")
#     else:
#      print("you guessed lower number ")
    
# print("game over")
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# joined_list = list1 + list2
# print(joined_list)

# list1 = [1,2,3]
# list2 = [1, 2, 3]
# list4 = list1*4
# print(list4)
# list3 = list1 + list2
# print(list3)


# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])
