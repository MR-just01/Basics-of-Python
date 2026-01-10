Word = ['apple' , 'banana' , 'cherry' , 'dog ' , 'elderberry']
filtered_words = [w.upper() for w in Word if len(w)>=4]

print("orginal list: " , Word)
print("filtered list : " , filtered_words)