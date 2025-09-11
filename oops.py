# ## student record 
# # class = blueprint or template 
# class student:
#     def __init__(self , name , grade):
#         self.name =name## attributes
#         self.grade = grade # attributes
      
#     def student_detils(self):
#      print(f"{self.name} is in the {self.grade}")


# stu_1 = student("madhavi" , 22)
# stu_2 = student("naman" , 1)
# # stu_1.student_detils() 
# print(stu_1.__dict__) ## it returns the result in the key value pairs
# print(stu_2.__dict__)

# # print(stu_1.name , stu_1.grade)


# # __init__ = it is a constructor , value initialize - fix 
# ## self is used to link the class and object , useed to built reffrence


# ###modify object 

# print(stu_1.name) 
# stu_1.name  = "Maya "
# print(stu_1.name)


# ##DELETION OF ATTRIBUTES
# del stu_1.grade




## 4 pillars of object oriented programming 

# 1. ABSTRACTION = hiding the unnecessary details of the class 



# class my_class:
#    def __init__(self, name , age):
#       self.name = name
#       self.age = age
#    def class_details(self): ## this method is kept hide from the user
#       print(f"{self.name} is {self.age} years old")

      
# cls1 = my_class("maya", 21)  #abstraction
# cls1.class_details()





# 2.ENCAPSULATION: 
# class my_class:
#    def __init__(self, name , age ,percentage):
#       self.name = name
#       self.age = age
#       self.__percentage = percentage ## double underscore limit the acess .. means we can cannot use this directly beacuse it id private now
    
#    def get_percentage(self):  # during decapsulating the best method is start the function with get so that it can give idea to the user that this attribut is encapsulated
#       return self.__percentage #only way to access the private members
      
   
#    def class_details(self): 
#       print(f"{self.name} is {self.age} years old and  have {self.__percentage}%")

      
# cls1 = my_class("maya", 21, 56)  
# cls1.class_details()
# # cls1.__percentage()   we cannot acess the private data member directly no matter what
# cls1.get_percentage()


## 3. INHERITANCE: 
## ALLOWS one class(child) to reuse the properties and methods of another class(parents)

# #parents class 
# class my_class:
#    def __init__(self, name , age):
#       self.name = name
#       self.age = age
#    def class_details(self): 
#       print(f"{self.name} is {self.age} years old")

#        # object
# cls1 = my_class("maya", 21) 
# cls1.class_details()

# ##child class 
# class stu_more(my_class): #stu_more is child class which id inheriting properties and methods from my_class
#    def __init__(self, name, age, branch): ## includes the parameters from the parents class and also includes the parameters of its own class
#       super().__init__(name, age)# calls the parent  class
#       self.branch = branch ## new attribute in the child class

# childclas1 = stu_more("meenu" , 32 , "cse")
# print(childclas1.branch)
# childclas1.class_details()

#3. POLYMORPHISM :


class student:
    def __init__(self , name , grade):
        self.name =name## attributes
        self.grade = grade # attributes
      
    def student_details(self):
     print(f"{self.name} is in the {self.grade}")

class child:
   def __init__(self, name , grade , age):
      self.name = name
      self.grade = grade
      self.age = age 
   def student_details(self):
      print(f"{self.name} is in {self.grade} with {self.age} years old " )
      
stu_1 = student("madhavi" , 12)
stu_1.student_details()
obj1 = child("maya", "btech" , 21)
obj1.student_details()