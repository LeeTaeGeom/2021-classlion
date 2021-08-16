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
    path('<int:post_id>/create_comment',create_comments,name="create_comments"),
    path('<int:post_id>/comment_edit/<int:comment_id>',comment_edit,name="comment_edit"),
    path('<int:post_id>/update_comments/<int:comment_id>',update_comments,name="update_comments"),
    path('<int:post_id>/delete_comments/<int:comment_id>',delete_comments,name="delete_comments"),
    path('like_toggle/<int:post_id>/',like_toggle, name="like_toggle"),
    path('dislike_toggle/<int:post_id>/',dislike_toggle, name="dislike_toggle"),
    

]