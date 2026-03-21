import json

student = {"name": "Jean", "age": 20 , "grade": "A"}
with open("student.json", "w") as file:
    json.dump(student, file)
with open("student.json", "r") as file:
    loaded_student = json.load(file)
print(loaded_student)

print(loaded_student["name"])
#writing and Reading a List to a File
students = ["Jean", "Alice", "Bob", "David"]
with open("students.txt", "w") as file:
    for student in students:
        file.write(student + "\n")
        students_from_file = []
        with open("students.txt" , "r") as file:
            for line in file:
             students_from_file.append(line.strip())
        print(students_from_file)        



       



    