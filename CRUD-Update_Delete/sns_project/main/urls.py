from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [

    path('',showmain, name="cover"),
    path('intro/',showintro, name="intro"),
    path('hobby/',showhobby, name="hobby"),
    path('food/',showfood, name="food"),
    path('netflix/',shownetflix, name="netflix"),
    path('new/',new, name="new"),
    path('create/', create, name="create"),
    path('<int:id>',showpost, name="showpost"),
    path('postlist/', postlist ,name="postlist"),
    path('edit/<int:id>', edit , name="edit"),
    path('update/<int:id>', update ,name="update"),
    path('delete/<int:id>', delete ,name="delete"),

]