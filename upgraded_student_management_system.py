import json

students = []


# ===== FILE HANDLING FUNCTIONS =====

def save_data():
    """Save the students list to students.json"""
    with open("students.json", "w") as file:
        json.dump(students, file)


def load_data():
    """Load the students list from students.json if it exists"""
    global students
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
        print("Data loaded successfully!")
    except FileNotFoundError:
        students = []
        print("No previous data found. Starting fresh.")


# ===== STUDENT FUNCTIONS =====

def add_student():
    name = input("Enter student name: ")
    math = float(input("Enter math score: "))
    english = float(input("Enter english score: "))
    science = float(input("Enter science score: "))

    student = {
        "name": name,
        "math": math,
        "english": english,
        "science": science
    }

    students.append(student)
    save_data()  # save after adding
    print("Student added successfully!\n")


def view_student():
    if not students:
        print("No students available yet.\n")
        return

    print("\n--- Student List ---")
    for s in students:
        print("Name:", s["name"])
        print("Math:", s["math"])
        print("English:", s["english"])
        print("Science:", s["science"])

        # NEW: calculate total, average and grade
        total = s["math"] + s["english"] + s["science"]
        average = total / 3
        grade = calculate_grade(average)

        print("Total:", total)
        print(f"Average: {average:.2f}")
        print("Grade:", grade)
        print("-------------------------\n")


def search_name():
    if not students:
        print("No student available to search.\n")
    else:
        search_name = input("Enter student name to search: ")
        found = False
        for s in students:
            if search_name.lower() == s["name"].lower():
                print("\n--- Student Found ---")
                print("Name:", s["name"])
                print("Math:", s["math"])
                print("English:", s["english"])
                print("Science:", s["science"])

                total = s["math"] + s["english"] + s["science"]
                average = total / 3
                grade = calculate_grade(average)

                print("Total:", total)
                print(f"Average: {average:.2f}")
                print("Grade:", grade)
                print("-------------------------\n")

                found = True
                break
        if not found:
            print(f"No student named '{search_name}' found.\n")


def update_student():
    if not students:
        print("No students available to update.\n")
        return

    name_to_update = input("Enter student name to update: ").lower()

    for s in students:
        if s["name"].lower() == name_to_update:
            print("\nStudent found! Enter new scores:")

            s["math"] = float(input("New Math score: "))
            s["english"] = float(input("New English score: "))
            s["science"] = float(input("New Science score: "))

            save_data()  # save after updating
            print("\nRecord updated successfully!\n")
            return

    print(f"No student named '{name_to_update}' found.\n")


def remove_student():
    if not students:
        print("No student available to remove.\n")
        return

    name_to_remove = input("Enter student name to be removed: ").lower()
    found = False

    for s in students:
        if s["name"].lower() == name_to_remove:
            students.remove(s)
            save_data()  # save after removing
            print("\nStudent removed successfully!\n")
            found = True
            break

    if not found:
        print(f"No student named '{name_to_remove}' found.\n")


def highest_scorer():
    if not students:
        print("No students available yet.\n")
        return

    top_student = max(
        students,
        key=lambda s: s["math"] + s["english"] + s["science"]
    )
    total = top_student["math"] + top_student["english"] + top_student["science"]
    average = total / 3
    grade = calculate_grade(average)

    print("\n=== Highest Scorer ===")
    print("Name:", top_student["name"])
    print("Math:", top_student["math"])
    print("English:", top_student["english"])
    print("Science:", top_student["science"])
    print("Total Score:", total)
    print(f"Average: {average:.2f}")
    print("Grade:", grade)
    print("========================\n")


def calculate_grade(avg):
    """Return grade based on average score."""
    if avg >= 70:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 45:
        return "D"
    else:
        return "F"


# ===== MAIN PROGRAM =====

load_data()  # Load saved students at start

while True:
    print("==== MENU ====")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search")
    print("4. Update")
    print("5. Remove student")
    print("6. Top scorer")
    print("7. Exit")

    choice = input("Enter (1/2/3/4/5/6/7): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        search_name()
    elif choice == "4":
        update_student()
    elif choice == "5":
        remove_student()
    elif choice == "6":
        highest_scorer()
    elif choice == "7":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid input. Please enter (1/2/3/4/5/6/7): \n")