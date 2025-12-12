from fastapi import HTTPException, Depends, APIRouter
from FastApiCourse.db.models import TeacherRating
from FastApiCourse.db.schema import  TeacherRatingSchema
from FastApiCourse.db.database import SessionLocal
from sqlalchemy.orm import Session
from typing import List


async def get_db():
    db = SessionLocal()
    try:
        yield  db
    finally:
        db.close()


rating_router = APIRouter(prefix='/teacher_rating', tags=['TeacherRating'])


@rating_router.post('/', response_model=dict)
async def create_teacher_rating(review: TeacherRatingSchema, db: Session = Depends(get_db)):
    rating = TeacherRating(**review.dict())
    db.add(rating)
    db.commit()
    db.refresh(rating)
    return {'message': 'Saved'}


@rating_router.delete('/{rating_id}')
async def teacher_rating_delete(rating_id: int, db: Session = Depends(get_db)):
    rating_db = db.query(TeacherRating).filter(TeacherRating.id == rating_id).first()
    if rating_db is None:
        raise HTTPException(status_code=404, detail='Rating Deleted')

    db.add(rating_db)
    db.commit()
    return {'message': 'Deleted'}