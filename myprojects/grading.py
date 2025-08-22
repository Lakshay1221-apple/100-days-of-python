# The Grading Criteria Project

def grading_criteria():
    print("Welcome to the grading criteria!")
    print("This program will help you determine the grade based on the marks entered.")

    students = {}

    # Input phase
    while True:
        name = input("\nEnter the name of the student: ").strip()

        if name in students:
            print("This name has already been used. Please enter a different name.")
            continue

        try:
            grade = int(input("Enter the marks of the student (0-100): "))
            if not (0 <= grade <= 100):
                print("Invalid marks. Please enter a value between 0 and 100.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        students[name] = grade

        # Strict validation for yes/no
        while True:
            another = input("Do you want to enter another student? (yes/no): ").strip().lower()
            if another in ("yes", "no"):
                break
            print("Invalid input. Please enter 'yes' or 'no'.")

        if another == "no":
            break

    # Grade assignment
    print("\n--- Grade Results ---")
    for student, grade in students.items():
        if grade >= 90:
            letter = 'A'
        elif grade >= 80:
            letter = 'B'
        elif grade >= 70:
            letter = 'C'
        elif grade >= 60:
            letter = 'D'
        elif grade >= 50:
            letter = 'E'
        else:
            letter = 'F'

        print(f"{student} has received grade {letter}.")

    # Optional: Personal check
    while True:
        check = input("\nDo you want to check the marks of a specific student? (yes/no): ").strip().lower()

        if check != 'yes' and check != "no":
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue

        if check == "no":
            break

        name_to_check = input("Enter the name of the student to check: ").strip()
        if name_to_check in students:
            print(f"{name_to_check} scored {students[name_to_check]} marks.")
        else:
            print("No such student found.")

# Loop to run program multiple times
while True:
    grading_criteria()
    again = input("\nDo you want to run the program again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for using the grading criteria program! Goodbye!")
        break
