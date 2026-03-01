from . import views
from django.urls import path
urlpatterns = [
    
    path('',views.teacher_list ,name="all-teachers"),
    path("addteacher",views.add_teachers ,name="addteachers"),
    path("update-teachers/<str:id>",views.update_teachers,name="update"),
    path("delete/<int:id>/", views.delete_teachers, name="delete"),
]