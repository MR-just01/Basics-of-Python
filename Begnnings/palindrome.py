def is_palindrome(number):
    return str(number) == str(number)[::-1]


num =  int(input("Enter the number you want to check"))
result = is_palindrome(num)
if (result == True):
    print(f"{num} is the palindrome")
else:
    print("not  palindrome "
          )
