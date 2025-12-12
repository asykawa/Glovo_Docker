import sys
from pathlib import Path
ROOT_DIR = Path(__file__).resolve().parent
sys.path.append(str(ROOT_DIR.parent))
from fastapi import FastAPI
import uvicorn
from starlette.middleware.sessions import SessionMiddleware
from FastApiCourse.admin.setup import setup_admin
from FastApiCourse.api import cart, favorite, certificate, course_review, social_auth
from FastApiCourse.api import category, lesson, course, assigment, auth, history, network, exam
from FastApiCourse.config import SECRET_KEY


course_app = FastAPI()
course_app.include_router(category.category_router)
course_app.include_router(auth.auth_router)
course_app.include_router(network.network_router)
course_app.include_router(lesson.lesson_router)
course_app.include_router(course.course_router)
course_app.include_router(cart.cart_router)
course_app.include_router(favorite.favorite_router)
course_app.include_router(assigment.assignment_router)
course_app.include_router(certificate.certificate_router)
course_app.include_router(exam.exam_router)
course_app.include_router(course_review.course_review_router)
course_app.include_router(history.history_router)
course_app.include_router(social_auth.social_router)



course_app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)
setup_admin(course_app)

















if __name__ == '__main__':
    uvicorn.run(course_app, host='127.0.0.1', port=8080)