#insertion sort in python
array = [12, 155, 10,9,3,5]
print("array before sorting : " ,array) 
for i in range(1,len(array)):
    key = array[i]
    j=i-1
    while j>=0 and array[j]>key:
        array[j+1] = array[j]
        j-=1
        array[j+1] = key

print("array after sorting : " ,array)

# ##selection sort 
array = [12, 155, 10,9,3,5]
print("array before sorting : " ,array)
for i in range(len(array)):
    min = i
    for j in range(i+1 , len(array)):
        if array[j]<array[min]:
            min = j

    array[i],array[min] = array[min],array[i] #swapping withour using the third variable 

  

print("array after sorting : " ,array)