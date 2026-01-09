file = open("sample.txt" , "r")
for line in file:
    line = line.strip()
    rev = ""
    for char in line:
        rev = char +rev
    print(rev)
file.close()