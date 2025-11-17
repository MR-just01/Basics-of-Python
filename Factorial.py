def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)


num = int(input("enter the number of you want factorial "))
factorial = fact(num)
print(f"factorial of {num} is : {factorial}")