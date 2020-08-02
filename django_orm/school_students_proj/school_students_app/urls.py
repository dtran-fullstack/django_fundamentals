from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('school',views.school),
    path('student',views.student),
    path('delete',views.delete)
]