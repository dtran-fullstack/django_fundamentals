from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('book/create', views.book_create),
    path('book/<int:book_id>',views.book_detail),
    path('book/<int:book_id>/add_author', views.book_add_author),
    path('authors',views.index2),
    path('author/create', views.author_create),
    path('author/<int:author_id>',views.author_detail),
    path('author/<int:author_id>/add_book', views.author_add_book),
]
