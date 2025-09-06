temp = float(input("Enter the temperature :"))
unit = input("celsius or fahenheit (C or F)")

if unit == "C":
    temp = (temp * 9/5)+32
    unit = "F"
    print(f"the temperature is : {temp}{unit}")
elif unit == "F":
    temp = (temp-32)*5/9
    unit = "C"
    print(f"the temperature is :{temp}{unit}") 
else:
    print("enter the valid unit")    