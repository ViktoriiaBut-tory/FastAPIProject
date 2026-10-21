from fastapi import FastAPI
from routers.students_routers import router as student_router
from routers.courses import router as course_router
from routers.items_router import router as item_router
from models.database import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
def home():
    return {"message": "this is main API home"}


app.include_router(student_router)
app.include_router(course_router)
app.include_router(item_router)
