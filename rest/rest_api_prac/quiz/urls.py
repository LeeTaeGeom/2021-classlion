from django.urls import path, include
from .views import *

app_name="quiz"

urlpatterns = [
    path("hello/",helloAPI,name="helloApi"),
    path("<int:id>/",randomQuiz,name="randomQuiz")
]
