def calculate_grade(student: student) -> str:
    if student.marks >= 90:
        return "A"
    elif student.marks >= 75:
        return "B"
    elif student.marks >= 60:
        return "C"
    elif student.marks >= 40:
        return "D"
    else:
        return "F"
def filter_passed_students(students: List[Student]) -> List[Student]:
    return [s for s in students if s.is_passed()]


def sort_by_marks(students: List[Student]) -> List[Student]:
    return sorted(students, key=lambda s: s.marks, reverse=True)
