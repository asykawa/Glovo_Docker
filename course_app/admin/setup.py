from .wews import UserProfileAdmin, CategoryAdmin, RefreshAdmin
from fastapi import FastAPI
from sqladmin import Admin
from course_app.db.database import engine


def setup_admin(store_app: FastAPI):
    admin = Admin(store_app, engine)
    admin.add_view(UserProfileAdmin)
    admin.add_view(CategoryAdmin)
    admin.add_view(RefreshAdmin)
