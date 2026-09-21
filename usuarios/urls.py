from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home),
    path("hola/<name>/", views.hello ),
    path("chau/", views.chau )
]
