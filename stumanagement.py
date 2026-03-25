import json 

def save(students):
   with open("students.json", "w") as file:
       json.dump(students, file)
def load():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except:
        return []
def show_menu():
    print("\n ===== Student Management System =====")
    print("1. Add a student")
    print("2. view all students")
    print("3. search for a student")
    print("4. delete a student")
    print("5. Update a student grade")
    print("6. Quit") 
def add_student(students):
    name = input("Enter name: ")
    age = input("Enter age: ")
    grade = input("Enter grade: ")
    student = {"name":name, "age": age, "grade": grade}
    students.append(student)
    print("DEBUG - reached this line")
    save(students)
    print(f"{name} added successfully!")
def view_students(students):
    if len(students) == 0:
        print("No students yet!")    
        return 
    for i, student in enumerate(students,1):
     print(f"{i}. Name: {student['name']} | Age: {student['age']} | Grade: {student['grade']}")
def search_student(students):
         name = input("Enter a name to search: ")
         for student in students:
             if student["name"].lower() == name.lower():
                 print(f"Found! Name: {student['name']} | Age: {student['age']} | Grade: {student['grade']}")
                 return
         print("student not found!")
def delete_student(students):
         name = input("Enter name to delete: ")
         for student in students:
             if student["name"].lower() == name.lower():
                 students.remove(student)
                 save(students)    
                 print(f"{name} deleted successfully!")
                 return
         print("Student not found!")

def update_grade(students):
             name = input("Enter name to update: ")
             for student in students:
                 if student["name"].lower() == name.lower():
                     new_grade = input("Enter new grade: ")
                     student["grade"] = new_grade
                     save(students)
                     print(f"{name}'s grade updated successfully!")
                     return
             print("student not found!")   
students = load()  
while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            update_grade(students) 
        elif choice == "6":
             print("Goodbye!")   
             break
        else:
             print("Invalid choice!")            