weight = float(input("Enter the weight:"))
unit = input("Kilogramn or pounds(kg /lbs)")

if unit == "kg":
    weight = weight*2.205 
    unit = "lbs"
    print(f"your weight is {weight}{unit}") 
elif unit == "lbs":
    weight = weight/2.205
    unit = "kg"
    print(f"your wieght is :{weight}{unit}")

else:
    print("Enter the valid Unit😭😭")
