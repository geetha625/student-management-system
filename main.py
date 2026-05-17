import json
students = []
def add_student():
    student_id = int(input("Enter student ID: "))
    name = input("Enter student name: ")
    marks = list(map(int, input("Enter 3 marks separated by spaces: ").split()))

    student = {
        "id": student_id,
        "name": name,
        "marks": marks
    }

    students.append(student)
    save_students()
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
        return

    print("\n Student Records ")

    for student in students:
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print("-" * 30)

def search_student():
    student_id = int(input("Enter student ID to search: "))

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            return

    print("Student not found.")

def update_student():
    student_id = int(input("Enter student ID to update: "))

    for student in students:
        if student["id"] == student_id:
            print("Student found!")

            student["name"] = input("Enter new name: ")
            student["marks"] = list(
                map(int, input("Enter new marks separated by spaces: ").split())
            )
            save_students()
            print("Student updated successfully!")
            return

    print("Student not found.")

def delete_student():
    student_id = int(input("Enter student ID to delete: "))

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students()
            print("Student deleted successfully!")
            return

    print("Student not found.")

def find_topper():
    if not students:
        print("No students found.")
        return

    topper = students[0]
    highest_total = sum(topper["marks"])

    for student in students[1:]:
        total = sum(student["marks"])

        if total > highest_total:
            topper = student
            highest_total = total

    print("\n🏆 Topper Details")
    print("ID:", topper["id"])
    print("Name:", topper["name"])
    print("Marks:", topper["marks"])
    print("Total Marks:", highest_total)

def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

def load_students():
    global students

    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        students = []
load_students()          
while True:
    print("\n Student Management System ")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Find Topper")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        find_topper()
    elif choice == "7":
        print("Thank you for using the Student Management System!")
        break
    else:
        print("Invalid choice. Please try again.")