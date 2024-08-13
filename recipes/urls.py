from django.urls import path
from recipes.views import home, contact, about


urlpatterns = [
    path('',home),
    path('sobre/',about),
    path('contato/',contact),
]