#class Student:
    #pass #empty for now 
class Student:
    #class vs instance variables
    school = "RCA"
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def is_passing(self):
        if self.grade in ["A", "B","C"]:
            return True
        else:
            return False
    def __str__(self):
        return f"name: {self.name} | age: {self.age} | grade: {self.grade}"    
        
    def new_grade(self, new_grade):
        self.grade = new_grade
        print(f"{self.name} 's grade updated to  {new_grade}")

class Teacher(Student):

  def __init__(self, name, age, grade):
      super().__init__(name, age, grade ="N/A")
      self.grade = grade
  def study(self):
      print(f"{self.name} is studying hard")
  def teacher_grade(self):
      print(f"{self.name} 's grade is {self.grade}")    

#methods are functions to our class. they take self as their first argument
student1 = Teacher("KAYTRANGA" , 17, "A")
print(student1.name)

student2 = Teacher("Ebra", 13, "A")
print(student2.age)
print(student1.is_passing())
student1.new_grade("B")
print(student1)
print(student1.school)
print(student2.school)
student1.study()
student2.is_passing()
student1.teacher_grade()

