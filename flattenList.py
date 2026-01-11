def  flatten(lst):
    flat_list = []
    for item in lst:
        if type(item) == list:
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

nested_list = [1,2,[3,4],[5,[6,7]] , 8]
result = flatten(nested_list)
print("Flattened List : " ,result)