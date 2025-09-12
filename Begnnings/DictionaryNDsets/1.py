# # dict = {
# #     "name" : "maya",
# #     "marks": [12,23,46,34] , 
# #     "cgpa" : 23.4
# # } 

# # dict["age"] = 24 #to add a new key:value in the dictionary 
# # print(dict,"\n"  )


# ##nested dictionary 
   
# stu_details = {
#     "name" : "joy",
#     "subjects" : {
#         "physics" : 13,
#         "chemistry" : 45,
#         "maths " : 56
#     } ,
#     "age" : {
#         "marcus" : 32,
#         "ginny" : 12
#     }
#  }  

# # print(stu_details["subjects"])  #prints the entire subject dictionary
# # print(stu_details["subjects"]["physics"]) #prints only physics key and value 



# ## dictionary methods 
# #keys() : returns the list of keys in the dict
# # print(list(stu_details.keys()))

# # values() : returns the list of values in the dict
# # print(list(stu_details.values()))


# #items(): it returns the key-value pairs from the dict 
# pair = list(stu_details.items())
# print(pair)

# #get(key): it returns the values accoding to the specific keys 
# get = (stu_details.get("name"))
# get2 = (stu_details.get("subjects"))
# get3 = stu_details.get("age")
# print(f"name of the student is : {get}")
# print(f"age  of the student is : {get3}")
# print(f"subjects of the student is : {get2}")


# # print(stu_details["username"])  ##error
# print(stu_details.get("username"))  ## instead of throwing an error it prints the none more used in the realcase scenarios

# ## update() : it is used in the existing dictionary 

# stu_details.update({'city' : 'jaipur'})
# print(stu_details)










### sets in the python 
#sets are the collection of the unique and immutable elements 

# collection = {23,13,23,12,3,4,'MAYA','Rawat' ,23}
# print(collection) ## does not allowed the duplicacy and does not have any order they are unorder 

# print(len(collection))

#sets methods 

# my_set = set()
 
# ## add() method is used to add the element in the set
# my_set.add("Rawat")  # we cannot add  list and dictionary in the sets 
# my_set.add(23)
# my_set.add(34)
# my_set.add("abcd")
# my_set.add(2)
# my_set.add((12,23,11,1))
# print(my_set)



## remove() method is used to remove element in the set 

# my_set.remove(2)
# print(my_set)

## clear () method is used to clear the whole set 

# my_set.clear()
# print(f"after usig the clear method :  {my_set}")


##pop method is used to pop any random value 
# my_set.pop()
# print(my_set)

#union() method :  it returns the unique elements  out of the given sets 
 
# set1 = {23,'maya' , 3.4 , 34}
# set2  =  { 23, 3.5 , 234 , 'Rawat '}
# set3 = {23 , 45, 'maya'}
# print(f" the union of  three sets are : {set1.union(set2,set3)}")
# print(set1) # beacause the elements of the sets are immutable i.e. cannot be changed 


# ## intersection () method : it returns the common elements from the given sets 
# set1 = {23,'Rawat' , 3.4 , 34}
# set2  =  { 23 , 234 , 'Rawat '}
# print(f" the intersection of  two sets are : {set1.intersection(set2)}")




# ## practice questions 
# dict : {
#      'cat' : 'a small animal',
#     'table' : ['a piece of a paper' , 'a list of facts and figures'] , 
   
# }

# print(dict)


#codex
# Write code below 💖
# weight = float(input("Enter your weight: "))
# planetnum = int(input("Enter the planet number (1-7) : "))

# if(planetnum == 1):
#   designwt = weight * 0.38
#   print(f"weight in the mercury :{designwt}")
# elif(planetnum == 2):
#   designwt = weight * 0.91
#   print(f"weight in the venus :{designwt}")
# elif(planetnum == 3):
#   designwt = weight * 0.38
#   print(f"weight in the mars :{designwt}")
# elif(planetnum == 4):
#   designwt = weight * 2.53
#   print(f"weight in the jupiter :{designwt}")
# elif(planetnum == 5):
#   designwt = weight * 1.07
#   print(f"weight in the saturn :{designwt}")
# elif(planetnum == 6):
#   designwt = weight * 0.89
#   print(f"weight in the uranus :{designwt}")
# elif(planetnum == 7):
#   designwt = weight * 1.14
#   print(f"weight in the neptune :{designwt}")
# else:
#   print("invalid planet number")


# answer = input("Are we there yet??")
# while answer != "yes" :
#   answer = input("Are we there yet??")
     
# print("yes we reach there")

# for i in range(10,0,-1):
#     print(i)
# print("Happy new year")

# import random 
# while True:
   
#  die1 = random.randint(1,6)
#  die2 = random.randint(1,6)
#  total = die1+die2
#  print(f"dice1 is rolled {die1}" )
#  print(f"dice2 is rolled {die2}" )
#  if (total == 2) :
#   print("Snake eyes")
#  else:
#   print("Nope")


# for i in range(1,25):
#     for j in range(i):
#         print("*",end = " ")
#     print()



# number = int(input("Enter the number : "))
# total = 0
# for i in range( 1,number+1):
#     total = total+i*i
# print("total is " , total)


# number = 345
# celsius  = (number -32)/1.8
# print(celsius)

mass = 48.8
height = 150
bmi = mass/height**2
print("bmi is " ,bmi)   