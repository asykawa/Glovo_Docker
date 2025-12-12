from fastapi import HTTPException, Depends, APIRouter
from FastApiCourse.db.models import Lesson
from FastApiCourse.db.schema import LessonCreateSchema
from FastApiCourse.db.database import SessionLocal
from sqlalchemy.orm import Session
from typing import List

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

lesson_router = APIRouter(prefix='/lesson', tags=['Lesson'])

@lesson_router.post('/', response_model=LessonCreateSchema)
async def lesson_create(lesson: LessonCreateSchema, db: Session = Depends(get_db)):
    lesson_db = Lesson(**lesson.dict())
    db.add(lesson_db)
    db.commit()
    db.refresh(lesson_db)
    return lesson_db


@lesson_router.delete('/{lesson_id}/')
async def delete_lesson( lesson_id: int, db: Session = Depends(get_db)):
    lesson_db = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if lesson_db is None:
        raise HTTPException(status_code=401, detail='Андай маалымат жок')
    db.delete(lesson_db)
    db.commit()
    return {'message': 'Deleted'}