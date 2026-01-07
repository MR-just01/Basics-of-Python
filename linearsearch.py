list = [12, 20, 10,30, 50, 40]
key = int(input("Enter the element to be searched: "))
isfound = False
for i in range(len(list)):
    if list[i] == key:
        print("Element found at index: " , i)
        isfound = True
        break
if not isfound:
    print("Element not found in the list")
