from django.urls import path
from . import views

urlpatterns = [
    path('',views.to_shows),
    path('shows/',views.main),
    path('shows/new',views.new),
    path('shows/create',views.new_process),
    path('shows/<int:show_id>',views.one_show),
    path('shows/<int:show_id>/edit', views.edit),
    path('shows/<int:show_id>/edit_process', views.edit_process),
    path('shows/<int:show_id>/delete', views.delete),
]