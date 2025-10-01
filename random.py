import random
game = ["scissor", "Rock"  , "paper"]
computer_choice = random.choice(game)

user_choice = input("Rock , paper or scissor??").lower
print(computer_choice)
if(user_choice == computer_choice):
    print("its a tie")
elif(user_choice == "rock" and computer_choice=="scissor" or \
   user_choice == "paper" and computer_choice == "rock" or \
   user_choice == "scissor" and computer_choice == "paper"):
    print("congratulations you win!!!")
elif(user_choice == computer_choice):
    print("its a tie")
else:
    print("opps computer win and you lose ")

 ##number guessing game 
import random
c_choice =random.randrange(1,7)

print("computer chose : " , c_choice)
attempt = 0 
max_attempt = 3
while(attempt<max_attempt):
    u_choice = int(input(f" Attempt {attempt+1} : Enter the number between 1 to 6 :"))
    attempt+=1
    if(u_choice == c_choice):
     print("you guessed the right number!!")
    elif(u_choice > c_choice):
     print("you guessed  higher number !!")
    else:
     print("you guessed lower number ")
    