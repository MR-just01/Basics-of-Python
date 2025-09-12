try:
    n= int(input("Enter the number : "))
    res = 100 / n
    
except ZeroDivisionError:
    print("can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")



    a = ["10", "twenty", 30]  
try:
    total = int(a[0]) + int(a[1]) 
    
except (ValueError, TypeError) as e:
    print("Error", e)
    
except IndexError:
    print("Index out of range.")



def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except ValueError as e:
    print(e)