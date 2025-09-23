import module as calc

##import the specific function 
from module import add


a=5 
b=6
print("addtion : " , calc.add(a,b))
print("subraction : " , calc.sub(a,b))
print("multiplication : " , calc.product(a,b))
print("division  : " , calc.div(a,b))

print(dir(calc))