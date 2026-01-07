list = [10 ,20, 30, 40,50, 60]
key = int(input("Enter the element to be searched : "))
low = 0 
high = len(list) -1
isfound = False 
while low<=high:
    mid = low + (high-low)//2
    if list[mid] == key:
        print("Element found at index : " , mid)
        isfound = True 
        break
    elif key<list[mid]:
        high = mid-1
    else:
        low = mid+1
if not isfound:
    print("Element not found in the list ")
    