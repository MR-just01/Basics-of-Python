# import os

# ##to see all the function in a module 
# print(dir(os))

# ## get me the current directory i am working on 

# print(os.getcwd())

# ## see the all file in the current directory
# print(os.listdir())


##creating the python module

def add(x,y):
    return x+y 
def sub(x,y):
    return x-y
def product(x,y):
    return x*y
def div(x,y):
    if(y==0):
        return "not possible "
    else:
        return x/y