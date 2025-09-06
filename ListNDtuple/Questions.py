#wap to store seven fruits in a list entered by the user
fruits = []
a = input("Enter the  fruits")
fruits.append(a)
b= input("Enter the fruits")
fruits.append(b)
c= input("Enter the fruits")
fruits.append(c)
d = input("Enter the fruits")
fruits.append(d)
e = input("Enter the fruits")
fruits.append(e)
f = input("Enter the  fruits")
fruits.append(f)
g = input("Enter the  fruits")
fruits.append(g)
print(fruits)

#wAP to accept marks of 6 students and display them in a sorted manner 
Marks = []
a = int (input("Enter the  Marks:"))
Marks.append(a)
b=  int(input("Enter the Marks:"))
Marks.append(b)
c=  int (input("Enter the Marks:"))
Marks.append(c)
d = int(input("Enter the Marks:"))
Marks.append(d)
e = int(input("Enter the Marks:"))
Marks.append(e)
f = int (input("Enter the  Marks:"))
Marks.append(f)
g = int(input("Enter the  Marks:"))
Marks.append(g)
Marks.sort()
print(Marks)

##wap to sum a list with 4 numbers 

l1 =[34,56,12,56]
print(sum(l1)) 

##wap to count the number of zeroes in the following tuple
#a=(7,0,8,0,0,9)
t1 = (7,0,8,0,0,9)
print(t1.count(0)) 












# guess =0 

# while guess !=6:
#     guess = int(input("Guess the number : "))
# print("you got it")

# for i in range( 1 ,101):
#   print(f"{i}I will not use Snapchat in class")


# for i in range(99 , 0, -1):
#   print(f"{i} bottles of beer on the wall ")
#   print(f"{i} bottles of beer ")
#   print("Take one down , pass it around")
#   print(f"{i-1} bottles of beer on the wall ")



# import random 
# num = random.randint(1,100)
# for  num in range (1,101):
#   if(num%3 == 0 and num%5 == 0 ):
#     print("FizzBuzz")
#   elif( num%3==0):
#     print("Fizz")
#   elif(num%5 == 0):
#     print('Buzz')
#   else:
#    print(num)


# import random

# lucky_number = random.randint(1, 9)
# not_found = True

# while not_found:
#   for i in range(1, 10):
#     if i == lucky_number:
#       not_found = False
#       break
#     else:
#       print(i)

# print(f"Yay I got my lucky number {lucky_number}! 🍀")

import random 
while True: 
 die1 = random.randint(1,6)
 die2 = random.randint(1,6)
 total = die1+die2
 print(f"dice1 is rolled {die1}" )
 print(f"dice2 is rolled {die2}" )
 if (total == 2) :
  print("Snake eyes")
  break
 else:
  print("Nope")