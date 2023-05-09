from django.urls import path

from . import views


app_name = "forums_board"

urlpatterns = [
    path('', views.index, name="index"),
]