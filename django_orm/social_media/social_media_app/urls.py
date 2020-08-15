from django.urls import path
from . import views

urlpatterns = [
    path('',views.render_login_register),
    path('login',views.login),
    path('logout', views.logout),
    path('register',views.register),
    path('wall',views.render_wall),
    path('post',views.post),
    path('profile/<int:uid>',views.profile),
    path('comment/<int:mess_id>',views.comment),
    path('edit/<mess_id>',views.edit),
    path('delete/<mess_id>',views.delete),
]