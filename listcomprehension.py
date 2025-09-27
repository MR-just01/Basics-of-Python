# ✅ Python Basics: Part-14  

# List Comprehensions & Looping Techniques 🔁🧠  

# List comprehension offers a cleaner and more concise way to create lists.

# 🔹 1️⃣ Basic List Comprehension  
 
squares = [x**2 for x in range(5)]  
print(squares)    # [0, 1, 4, 9, 16]


# 🔹 2️⃣ With Condition  
 
even = [x for x in range(10) if x % 2 == 0]  
print(even)  # [0, 2, 4, 6, 8]


# 🔹 3️⃣ Nested Loops in Comprehension  
 
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]  
print(pairs)  # [(1, 3), (1, 4), (2, 3), (2, 4)]


# 🔹 *4️⃣ Using if-else in Comprehension*  
 
labels = ['Even' if x % 2 == 0 else 'Odd' for x in range(5)]  
print(labels)  # ['Even', 'Odd', 'Even', 'Odd', 'Even']


# 🔹 5️⃣ Set Comprehension  
 
unique = {x for x in [1, 2, 2, 3]}  
print(unique)  # {1, 2, 3}


# 🔹 6️⃣ Dictionary Comprehension  
 
squares = {x: x**2 for x in range(4)}  
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9}


# 🔹 *7️⃣ Looping with enumerate()*  
 
for index, value in enumerate(['a', 'b']):  
    print(index, value)


# 🔹 *8️⃣ Looping with zip()*  
 
names = ['Ram', 'Shyam']  
scores = [85, 90]  
for name, score in zip(names, scores):  
    print(name, score)


