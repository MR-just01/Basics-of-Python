# functions without parameters 
# def greetings():
#     print("hello")

# greetings()    



# ## functions with parameters 
# def addNum(a,b):  ##parameters
#     c = a+b
#     print("the addition of 2 two is " , c)

# addNum(23,45) #arguements
# addNum(a=90,b=34)


## celsius to fahrenheit

def temp_converter(celsius):
    fahrenheit = (celsius*9/5)+32
    return fahrenheit

temp_f = temp_converter(38)
print(temp_f)


#pass statement 
def undefined():
    pass  # does nothinf for now 


#wap to create the calculator that can perform at least five operations and make user to input the prompt

print("-----------SIMPLE CALCULATOR--------")
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
operations = input("Ente the operation performed in the numbers (+ , - , * / ,% ) : ")

if(operations == '+' ):
    print(f"the sum of {num1} and  {num2} " , num1+num2)
elif(operations == '-'):
    print(f"the subraction of {num1} and  {num2} "  ,num1-num2)
elif(operations == '*'):
    print(f"the multiplication of {num1} and  {num2} "  ,num1*num2)
elif(operations == '/'):
    print(f"the division of {num1} and  {num2} "  ,num1/num2)
elif(operations == '%'):
    print(f"the modulus of {num1} and  {num2} "  ,num1%num2)
else:
    print("Enter the correct operators!!!")