import random 
easy = ["apple", "none"  ,"mango" , "india" , "property" , " coffee  , chai"]
meduim = ["achieve", "collaborate", "deceive", "diverse", "expand", "imagine"," inspire"," rational", "strategy"," subtle"]
hard = ["Anemone",
"Colonel",
"Onomatopoeia",
"Aberration",
"Abjure",
"Acquiesce",
"Cajole",
"Encumber",
"Epitome"
]
print("WElcome to the password guessing game ")
print("Choose the difficulty level :")
print("1. Easy")
print("2.meduim ")
print("3.hard")
level = input("Enter the Difficulty : " ).lower()
if level == "easy" :
    secret = random.choice(easy)
elif level == "meduim " : 
    secret = random.choice(meduim)
elif level == "hard":
    secret = random.choice(hard)
else:
    print("Invalid choice . Default to easy level")
    secret = random.choice(easy)

attempts  = 0 
print("\n Guess the secret password")
while True:
    guess = input("Enter your guess ").lower()
    attempts +=1
    
    if guess == secret:
        print(f"congratulations !!! you guesses it in {attempts} attempts.")
        break
    
    hint = ""
    for i in range (len(secret)):
        if i<len(guess) and guess[i] == secret[i]:
           hint += guess[i]
        else:
            hint += "_"
    print("hint : " ,hint)

print("Game over!!!:| ")
     

