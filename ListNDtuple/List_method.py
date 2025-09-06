exlist = [45, "maya","good", True ,56.7  ]
print(exlist)
exlist.append("HATE") #append method
print(exlist)

l1 = [2,4,62,1,5,657]
# l1.sort()  #sorting the number in the list using sort
# l1.reverse()  #reversing the list using reverse method 
# l1.insert(4,45) #Insert 45 such that its index in the list is 4
 
value = l1.pop(4) #pop out the number at the index 4 such as 5 in this list 
print(value)  # output = 5 ,return value
print(l1)  #output = [2,4,62,1,657]

l1.remove(657) # use to remove the particular number from the list 
print(l1) #output = [2,4,62,1]