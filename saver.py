def save_students(students):
    with open("student.txt", "w") as file:
        for student in students:
            file.write(student + "\n")
def append_student(name):
    with open("student.txt", "a") as file:
        file.write(name + "\n")      
def read_students():
    with open("student.txt" , "r") as file:
        for line in file:
            print(line.strip())

students = []
for i in range(1,4):     
    name = input(f"Enter student {i}: ")
    students.append(name)
    save_students(students)
    read_students()
new_student = input("Enter a new student: ")
append_student(new_student) 

read_students()                     