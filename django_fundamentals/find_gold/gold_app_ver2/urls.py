from django.urls import path
from . import views

urlpatterns = [
    path('',views.index2),
    path('reset',views.reset),
    path('<str:source_name>',views.process),
]