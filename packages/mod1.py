# class student:
#     def __init__(self , name , ROLLno, grade):
#         self.name = name 
#         self.ROLLno = ROLLno
#         self.grade = grade

#     def display(self):
#         print(f" student name is : {self.name}")
#         print(f"stdue{self.ROLLno}")
#         print(self.grade)

# result= student("maya",23 , 'A')
# result.display()

def student():
    name = input("enter the name of the student: ")
    print(name)
    age = int(input("enter your age : "))
    print(age)
    qualification = input("Highest qualification : 10th/12th/Diploma/Graduate : ")
    print(qualification)
student()