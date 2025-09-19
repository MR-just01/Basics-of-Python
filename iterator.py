

def my_generator():
    yield 1
    yield 8
    yield 3

for value in my_generator():
    print(value)




my_list = [1,7 ,6 ,7]

# my_iter = iter(my_list)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

# print(next(my_iter))  #StopIteration is exception has ocuured 

##create an iterator object from above iterable 
iter_obj = iter(my_list)

while True:
    try:
        element = next(iter_obj) ## get the next item from the iterator
        print(element)
    except StopIteration:
        break

    