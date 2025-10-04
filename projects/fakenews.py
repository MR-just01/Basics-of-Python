import random
subjects =[
    "Nirmala sitaraman",
    "openAI",
    "sonam wangchuk",
    "Harry porter",
    "prime minister",
    "democracy",
    "salmaan khan"
]

actions = [
    "launches ",
    "waits",
    "deer",
    "taxs",
    "celbrates",
    "vibe",
    "dangerous",
    "diplomatic",
    "dictatorship",
    "arrested"
]

mountains =[]

place_of_action =[
    "at the red fort",
    "during the drive",
    "in the parliament ",
    " at the parliamenr",
    "in the valley of ladak",
    " in the jail",
    "nowhere in the middle ",
    "at the baar "

]

while(True):
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_of_actions = random.choice(place_of_action)

    Headline = f"BREAKING NEWS : {subject} {action} {place_of_actions}"
    print("\n" + Headline)

    userinput = input("Do you want another headline (yes/no) : " ).strip().lower()
    if userinput == "no" :
     break

print("Thanks for using ")