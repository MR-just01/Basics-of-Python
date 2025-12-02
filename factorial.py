num = int(input("Enter the number to find factorial : "))
factorial = 1
i = 1
while i<=num:
    factorial = factorial *i
    i = i+1
print("the factorial of ", num ,  " is : ", factorial)