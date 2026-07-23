import numpy as np

# Initialize an empty list to store student records
# Each student record will be a dictionary
students = []

def display_menu():
    print("\n--- Student Analytics Menu ---")
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Update Student Record")
    print("4. Delete Student Record")
    print("5. Analyze Marks (NumPy)")
    print("6. Perform Matrix Operations on Marks")
    print("7. Generate Random Student Datasets")
    print("8. Filter Pass/Fail and Toppers")
    print("9. Apply Grace Marks")
    print("10. Exit")
    print("----------------------------")

def add_student():
    print("\n--- Add New Student ---")
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    # Marks will be a list of numbers
    marks_str = input("Enter Marks (comma-separated, e.g., 85,90,78): ")
    try:
        marks = [float(m.strip()) for m in marks_str.split(',') if m.strip()]
    except ValueError:
        print("Invalid marks format. Please enter numbers separated by commas.")
        return

    student_record = {
        'id': student_id,
        'name': name,
        'marks': marks
    }
    students.append(student_record)
    print(f"Student {name} (ID: {student_id}) added successfully.")

def view_students():
    print("\n--- All Student Records ---")
    if not students:
        print("No student records available.")
        return
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, Marks: {student['marks']}")

def update_student():
    print("\n--- Update Student Record ---")
    student_id = input("Enter the ID of the student to update: ")
    for student in students:
        if student['id'] == student_id:
            print(f"Found student: {student['name']}")
            new_name = input(f"Enter new name (current: {student['name']}): ")
            new_marks_str = input(f"Enter new marks (comma-separated, current: {student['marks']}): ")

            if new_name:
                student['name'] = new_name
            if new_marks_str:
                try:
                    student['marks'] = [float(m.strip()) for m in new_marks_str.split(',') if m.strip()]
                except ValueError:
                    print("Invalid marks format. Marks not updated.")
            print("Student record updated successfully.")
            return
    print(f"Student with ID {student_id} not found.")

def delete_student():
    print("\n--- Delete Student Record ---")
    student_id = input("Enter the ID of the student to delete: ")
    global students
    initial_len = len(students)
    students = [s for s in students if s['id'] != student_id]
    if len(students) < initial_len:
        print(f"Student with ID {student_id} deleted successfully.")
    else:
        print(f"Student with ID {student_id} not found.")

def analyze_marks():
    print("\n--- Analyze Marks ---")
    if not students:
        print("No student records available for analysis.")
        return

    all_marks = []
    for student in students:
        if student['marks']:
            all_marks.extend(student['marks'])

    if not all_marks:
        print("No marks data available for analysis.")
        return

    marks_array = np.array(all_marks)

    print(f"Total Marks Entries: {len(marks_array)}")
    print(f"Sum of Marks: {np.sum(marks_array):.2f}")
    print(f"Mean of Marks: {np.mean(marks_array):.2f}")
    print(f"Median of Marks: {np.median(marks_array):.2f}")
    print(f"Standard Deviation of Marks: {np.std(marks_array):.2f}")
    print(f"Minimum Mark: {np.min(marks_array):.2f}")
    print(f"Maximum Mark: {np.max(marks_array):.2f}")

def perform_matrix_operations():
    print("\n--- Perform Matrix Operations on Marks ---")
    print("This functionality will allow you to perform matrix operations on student marks (e.g., combining subject scores).")
    print("Coming soon!")

def generate_random_students():
    print("\n--- Generate Random Student Datasets ---")
    num_students = int(input("How many random students to generate? "))
    for i in range(num_students):
        student_id = f"R{len(students) + 1}"
        name = f"Random Student {len(students) + 1}"
        num_subjects = np.random.randint(3, 6) # 3 to 5 subjects
        marks = np.random.randint(40, 100, num_subjects).tolist()
        students.append({'id': student_id, 'name': name, 'marks': marks})
    print(f"{num_students} random students generated.")

def filter_students():
    print("\n--- Filter Pass/Fail and Toppers ---")
    if not students:
        print("No student records to filter.")
        return

    pass_threshold = float(input("Enter passing threshold (e.g., 50): "))
    topper_threshold = float(input("Enter topper threshold (e.g., 90): "))

    print("\n--- Passed Students ---")
    passed_count = 0
    for student in students:
        if student['marks'] and np.mean(student['marks']) >= pass_threshold:
            print(f"ID: {student['id']}, Name: {student['name']}, Avg Mark: {np.mean(student['marks']):.2f}")
            passed_count += 1
    if passed_count == 0:
        print("No students passed.")

    print("\n--- Topper Students ---")
    topper_count = 0
    for student in students:
        if student['marks'] and np.mean(student['marks']) >= topper_threshold:
            print(f"ID: {student['id']}, Name: {student['name']}, Avg Mark: {np.mean(student['marks']):.2f}")
            topper_count += 1
    if topper_count == 0:
        print("No toppers found.")

def apply_grace_marks():
    print("\n--- Apply Grace Marks ---")
    if not students:
        print("No student records to apply grace marks to.")
        return

    grace_amount = float(input("Enter grace marks to apply: "))

    for student in students:
        if student['marks']:
            marks_array = np.array(student['marks'])
            # Apply grace marks, ensuring marks don't exceed 100
            student['marks'] = (marks_array + grace_amount).clip(0, 100).tolist()
            print(f"Grace marks applied for {student['name']}. New Marks: {student['marks']}")
        else:
            print(f"No marks for {student['name']} to apply grace marks.")

def main_menu():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            analyze_marks()
        elif choice == '6':
            perform_matrix_operations()
        elif choice == '7':
            generate_random_students()
        elif choice == '8':
            filter_students()
        elif choice == '9':
            apply_grace_marks()
        elif choice == '10':
            print("Exiting Student Analytics System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main_menu()
