from fastapi import APIRouter
from models.students_model import Student

router = APIRouter()

students = [
    Student(id="101", name="a", course="IT"),
    Student(id="102", name="b", course="SW dev"),
    Student(id="103", name="c", course="SW dev"),
    Student(id="104", name="d", course="webd"),
    Student(id="105", name="e", course="webd"),
]


@router.post("/students")
def create_student(student: Student):
    students.append(student)
    return {"message": "Student added successfully", "students": students}


@router.get("/students")
def get_students(course: str = "none"):
    if course == "none":
        return students
    else:
        sts = [s for s in students if s.course == course]
        return sts


@router.put("/student/{student_id}")
def update_student(student_id: str, student: Student):
    exists = any(st.id == student_id for st in students)

    if exists:
        for index, s in enumerate(students):
            if s.id == student_id:
                students[index] = student
                return {"msg": "Record updated successfully"}

    return {"msg": "Student not found"}


@router.delete("/student/{student_id}")
def delete_student(student_id: str):
    exists = any(st.id == student_id for st in students)

    if exists:
        for index, s in enumerate(students):
            if s.id == student_id:
                students.pop(index)
                return "Record delete successfully"
    else:
        return "not found"


@router.get("/student/{student_id}")
def get_student(student_id: str):
    for student in students:
        if student.id == student_id:
            return student

    return {"message": "Student not found"}
