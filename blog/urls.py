from .views import *

from django.urls import path

app_name = "blog"

urlpatterns = [
    path('', index , name="index"),
]
