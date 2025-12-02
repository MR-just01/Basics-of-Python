a = int(input("Enter  first integer: "))
b= int(input("Enter  second  integer: "))
c = int(input("Enter  third integer: "))

if(a<b and a<c):
    if(b<c):
        min, mid , max = a, b,c
    else:
        min , mid, max = a,c,b
if(b<c and b<a):
    if(a<c):
        min , mid, max = b,a,c
    else:
        min , mid ,max = b,c,a
if(c<a and c<b):
    if(a<b):
        min , mid , max  = c,a,b
    else:
        min ,mid, max = c,b, a

print("The intergrs in ascending order are : ", min , mid ,max)


