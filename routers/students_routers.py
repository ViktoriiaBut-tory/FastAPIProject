from fastapi import APIRouter
from models.students_model import Student

router = APIRouter()

students = [
    Student(id="104", name="a", course="IT"),
    Student(id="105", name="2", course="SW"),
]


@router.post("/students")
def create_student(student: Student):
    students.append(student)
    return {"message": "Student added successfully", "students": students}


@router.get("/students")
def get_students():
    return students


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
