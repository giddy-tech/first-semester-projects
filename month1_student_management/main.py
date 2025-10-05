from student_data import add_student, view_students, get_average_grade

def main():
    while True:
        print("=== 🎓 Student Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Calculate Average Grade")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            get_average_grade()
        elif choice == '4':
            print("\n👋 Exiting program. Goodbye!\n")
            break
        else:
            print("\n❌ Invalid choice, please try again.\n")


if __name__ == "__main__":
    main()
