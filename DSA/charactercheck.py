file = open("sample.txt" , "r")
text = file.read()
file.close()
words = len(text.split())
characters = len(text)
lines = text.count('\n')+ 1

print("Number of lines: ", lines )
print("Number of words: " , words)
print("number of  characters : " , characters)