def remove_dup (items):
    seen = set()
    result = []

    for i in items :
        if i not in seen:
            result.append(i)
            seen.add(i)
    return result 

nums = [1,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,7,1,1,1,8]
print(f"clean list is : " , remove_dup(nums))
