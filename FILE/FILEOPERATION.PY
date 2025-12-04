##FILE HANDLING
## modes:r- read and write:w, append = a


#OPENING THE FILE 
file = open('TEST.txt' , 'r')

# READING THE FILE 
file = open('TEST.txt' , 'r')
content = file.read() #read entire data
print(content)
file.close()

#USING THE READLINE FUNCTION

file = open('TEST.txt' , 'r')
content = file.readline() ##only reads the first line of file 
print(content)
file.close()

# ##USING THE READLINES METHOD
file = open('TEST.txt' , 'r')
content = file.readlines() ##give output in he list form after every new line   
print(content)
file.close()

#----------------------WRITE MODE----------------------

# #write the file 
file = open('TEST2.txt' , 'a') ## it overwrite
file.write("namaste london ")
file.write("is the great rom-com")
file.close()

# ## append method help to prevent from the overidding in the file 
file = open('TEST2.txt' , 'a')
file.write("\nmovie")
file.write("\nkat is a great actor")
file.close()

##closing a file 


file = open('TEST2.txt' , 'r+')
file.write("\n this is written in read and write mode ")
content = file.readlines() 
content = file.read()
file.close()

#using with statement 
with open('TEST.txt' , 'r')as file :
    content = file.read()
    print(content)





