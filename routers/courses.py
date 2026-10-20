from fastapi import APIRouter

router = APIRouter()

courses = [
    {"cid": "1", "title": "Web development"},
    {"cid": "2", "title": "Software testing"},
    {"cid": "3", "title": "Web design"},
    {"cid": "4", "title": "Data analysis"},
]


@router.get("/")
def home():
    return {"msg": "this is course api"}


@router.get("/courses")
def allcourses():
    return courses


@router.get("/courses/{course_id}")
def gercourse(course_id: str):
    course = "not found"
    for c in courses:
        if c["cid"] == course_id:
            course = c
            break
    return {"course": course}
