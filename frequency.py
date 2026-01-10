from collections import Counter 

def frequency(input_string):
    clean_text = input_string.lower().replace(" ", " ")

    return Counter(clean_text)

text = "python programming"
freq = frequency(text)
print("orginal text : " , text)
print("character frequency : " , freq )
