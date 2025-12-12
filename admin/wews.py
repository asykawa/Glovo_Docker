from FastApiCourse.db.models import UserProfile, Category, Refresh
from sqladmin import ModelView

class UserProfileAdmin(ModelView, model=UserProfile):
    column_list = [UserProfile.first_name, UserProfile.last_name]


class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.category_name]


class RefreshAdmin(ModelView, model=Refresh):
    column_list = [Refresh.id]


