from django.urls import path
from .views import *

urlpatterns = [
    path("", Index, name="index"),
    path("contact/", Contact, name="contact"),
    path("categories/", Categories, name="categories")
]