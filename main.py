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
        print("Update Student selected")
    elif choice == "5":
        print("Delete Student selected")
    elif choice == "6":
        print("Find Topper selected")
    elif choice == "7":
        print("Thank you for using the Student Management System!")
        break
    else:
        print("Invalid choice. Please try again.")