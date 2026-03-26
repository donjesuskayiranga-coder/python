#lass Student:
    #pass #empty for now 

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

student1 = Student("KAYTRANGA" , 17, "A")
print(student1.name)