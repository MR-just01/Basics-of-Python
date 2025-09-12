# friend =["everything " , " apple " , 5,45.6 ,False , True ]
# print(friend[0])
# friend[0] = "nothing" # unlike string lists are mutable 
# print(friend[0])

# #slicing in the list is same as in the string 
# print(friend[2:4]) #prints 5 and 45.6


# student  = [12,34,56,67,234,233]
# print(student[-4:-2 ])

# list methods 
# list = ["maya","hello","heay"]
# # list.sort()
# list.reverse()
# print(list)

# stud  = [12,34,56,67,233,234,233]
# # stud.sort(reverse=True)
# # stud.insert(2,24)
# # stud.remove(233)
# stud.pop(1)  
# print(stud)

# movies = [] 
# mov1 = input("Enter the first movie")
# mov2 = input("Enter the second movie")
# mov3 = input("Enter the third movie")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)


lis1 = [1,2,1]
list2 = [1,4,12,3]
copy_List = lis1.copy()
copy_List.reverse()
if(copy_List == lis1):
    print("Palidrome")
else:
    print("not palidrome")