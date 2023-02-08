class Student:
# Conctructor
    def __init__(self,name,rollNumber):
        if name !="":
            self.name = name                
        else:
            print("Invalid Name")
        if rollNumber >= 0:
            self.rollNumber = rollNumber
        else:
            print("Invalid Roll Number")
        

#creating Student instances
student1 = Student("Niranjan",543) 
student1 = Student("Zero",000) 

        