def display_student(student: Student):
    grade = calculate_grade(student)
    print(f"Name: {student.name}, Age: {student.age}, Marks: {student.marks}, Grade: {grade}, Address: {student.address}")


def display_all(students: List[Student]):
    print("\n=== Student Results ===")
    for s in students:
        display_student(s)
