students = {}   # empty dictionary

while True:
    print("\n--- Student Grades Menu ---")
    print("1. Add new student")
    print("2. Update student grade")
    print("3. Print all student grades")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        print("Student added successfully!")

    elif choice == 2:
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print("Grade updated successfully!")
        else:
            print("Student not found!")

    elif choice == 3:
        if len(students) == 0:
            print("No students available.")
        else:
            print("\n--- All Student Grades ---")
            for name, grade in students.items():
                print(f"{name} : {grade}")

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
