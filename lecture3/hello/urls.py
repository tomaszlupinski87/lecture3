from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("tomek", views.tomek, name="Tomek"),
    path("<str:name>", views.greet, name="greet"),
]