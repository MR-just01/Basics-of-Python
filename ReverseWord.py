def reverseIndi(sentence):
    words = sentence.split()

    reversed_words = [word[::-1] for word in words]

    return " ".join(reversed_words)

text = "python is fun with code "
result = reverseIndi(text)
print("Original Sentence : " , text)
print("Reversed Individual Words : " ,result)
