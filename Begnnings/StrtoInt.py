str = input("enter the number")
print(type(str))
int_num = int(str)
print(type(int_num))
print(int_num)


#area of the reactagle

def area_rect( lenght , width):
    return lenght*width



l = float(input("Enter the lenght: "))
b =float(input("Enter the width: "))

area = area_rect(l ,b)
print(f"area of the rectanle with {l} and {b} is: {area}")
