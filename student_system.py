students = []


# Add Student
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    try:
        marks = int(input("Enter marks: "))
    except ValueError:
        print("Marks must be numbers!")
        return

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")


# View Students
def view_students():
    if len(students) == 0:
        print("No students available")
    else:
        print("\nStudent Records:")
        for s in students:
            print("-------------------")
            print("Name :", s["name"])
            print("Roll :", s["roll"])
            print("Marks:", s["marks"])


# Search Student
def search_student():
    roll = input("Enter roll number to search: ")

    for s in students:
        if s["roll"] == roll:
            print("Student Found")
            print(s)
            return

    print("Student not found")


# Update Marks
def update_marks():
    roll = input("Enter roll number: ")

    for s in students:
        if s["roll"] == roll:
            try:
                new_marks = int(input("Enter new marks: "))
            except ValueError:
                print("Invalid marks")
                return

            s["marks"] = new_marks
            print("Marks updated successfully")
            return

    print("Student not found")


# Delete Student
def delete_student():
    roll = input("Enter roll number to delete: ")

    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted successfully")
            return

    print("Student not found")


# Main Menu
while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_marks()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Program exited")
        break

    else:
        print("Invalid choice")