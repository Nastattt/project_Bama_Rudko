from django.urls import path

from app import views

urlpatterns = [
    path("", views.all_films, name="all-films"),
    path("films/<int:pk>", views.detail_film, name="detail-film"),

    path("add", views.create_film, name="add-film"),
    path("edit/<int:pk>", views.edit_film, name="edit-film"),
    path("delete/<int:pk>", views.delete_film, name="delete-film"),
]
