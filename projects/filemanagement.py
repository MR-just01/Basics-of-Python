import os 

def create_file(filename):
    try:
        with open(filename , 'x') as f:
            print(f"file name : {filename} : created sucessfully !!")      #with is used to close the file after completing the work in that file
    except FileExistsError : 
        print(f"file name {filename} already exist!!")  
    except Exception as E : 
        print("an error occurred!!")

def viewallfile():
    file = os.listdir()
    if not file : 
        print("no file found !!")
    else:
        print("file in directory !!")
        for files in file : 
            print(file )

def deletefile(filename ):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully!!")
    except FileNotFoundError:
        print("file not found ")
    except Exception as e :
        print("sn error occurred")

def readfile(filename):
    try:
        with open('sample.txt ' , 'r') as f :
            content = f.read()
            print(f"content of {filename} : \n {content} ")
    except FileNotFoundError:
        print("file not found ")
    except Exception as e:
        print("an error occured ")

def editfile(filename):
    try:
        with open('sample.txt' , 'a') as f:
            content = input("enter the data to addup  = ")
            f.write (content + "\n")
            print("content added to {filename } successfully ")
    except FileNotFoundError : 
        print(f"{filename } doesn't exist ")
    except Exception as e:
        print("an erroe is occured!!!")





def main():
    while True:
        print("FILE MANAGEMENT APP")
        print("1.create a file :")
        print("2.View all files ")
        print("3. Delete the file ")
        print("4.Read file ")
        print("5. Edit the file ")
        print("6. exit")

        choice = int(input("Enter the choice : "))
        if choice == 1:
            filename = input("enter the file name to create : ")
            create_file(filename)
        if choice == 2: 
            viewallfile()
        if choice == 3:
            filetodel = input("Enter the file to be deleted")
            deletefile(filetodel)
        if choice == 4:
            filetoread = input("enter the file to read")
            readfile(filetoread)

        if choice == 5:
            filetoedit = input("enter th file to delete : ")
            editfile(filetoedit)
        if choice == 6:
            print("exiting the program ")
            break
        else:
            print("invalid") 



if __name__ == "__main__":
    main()
