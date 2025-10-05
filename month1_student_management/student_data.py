students = []  # List to store student records

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = float(input("Enter student grade: "))

    student = {
        "name": name,
        "age": age,
        "grade": grade
    }
    students.append(student)
    print(f"\n✅ {name} added successfully!\n")


def view_students():
    """Print all students"""
    if not students:
        print("\n⚠️ No students added yet.\n")
        return

    print("\n📋 Student List:")
    for i, student in enumerate(students, 1):
        print(f"{i}. {student['name']} | Age: {student['age']} | Grade: {student['grade']}")
    print()


def get_average_grade():
    """Return the average grade"""
    if not students:
        print("\n⚠️ No students to calculate average.\n")
        return

    total = sum(student["grade"] for student in students)
    average = total / len(students)
    print(f"\n📊 Average Grade: {average:.2f}\n")
