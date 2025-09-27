def qualified():

    cgpa = int(input("enter your CGPA : "))
    if(cgpa >= 9):
     print("qualified")
    else:
     projects = input("do you have github acc:")
     if(projects == "yes"):
       print("qualified")
     else:
       print("better luck next time")

qualified()
