from django.shortcuts import render, redirect,get_object_or_404
from  .models import Post, Comment
from django.utils import timezone
import random
# Create your views here.

def showmain(request):
    return render(request, 'main/cover.html')

def postlist(request):
    posts=Post.objects.all()
    return render(request, 'main/postlist.html',{'posts':posts})

def showintro(request):
    return render(request, 'main/intro.html')

def showhobby(request):
    return render(request, 'main/hobby.html')

def shownetflix(request):
    return render(request, 'main/netflix.html')

def showfood(request):
    return render(request, 'main/food.html')
    
def showpost(request,id):
    post = get_object_or_404(Post, pk =id)
    all_comments = post.comments.all().order_by('-created_at')
    return render(request,'main/detail.html',{'post':post, 'comments':all_comments})

def new(request):
    return render(request,'main/new.html')

def create(request):
    new_post = Post()
    new_post.title=request.POST['title']
    new_post.writer=request.user
    new_post.pub_date=timezone.now()
    new_post.body=request.POST['body']
    new_post.image = request.FILES.get('image')
    new_post.save()
    return redirect('main:showpost',new_post.id)

def edit(request, id):
    edit_post=Post.objects.get(id=id)
    return render(request, 'main/edit.html',{'post':edit_post})

def update(request, id):
    update_post = Post.objects.get(id=id)
    update_post.title = request.POST['title']
    update_post.writer = request.user
    update_post.pub_date = timezone.now()
    update_post.body = request.POST['body']
    update_post.image = request.FILES.get('image')
    update_post.save()
   
    return redirect('main:showpost', update_post.id)

def delete(request,id):
    delete_blog = Post.objects.get(id=id)
    delete_blog.delete()
    return redirect('main:postlist')

def create_comments(request,post_id):
    new_comment=Comment()
    new_comment.content=request.POST['content']
    new_comment.writer=request.user
    new_comment.post=get_object_or_404(Post,pk=post_id)
    new_comment.save()
    return redirect('main:showpost',post_id)

def comment_edit(request,post_id,comment_id):
    edit_comment=Comment.objects.get(id=comment_id)
    return render(request, 'main/comment_edit.html',{'comment':edit_comment,'post_id':post_id})


def update_comments(request,post_id,comment_id):
    update_comment=Comment.objects.get(id=comment_id)
    update_comment.content=request.POST['content']
    update_comment.writer=request.user
    update_comment.post=get_object_or_404(Post,pk=post_id)
    update_comment.save()
    return redirect('main:showpost',update_comment.post.id)

   
def delete_comments(request,post_id,comment_id):
    
    delete_comment = Comment.objects.get(id=comment_id)
    delete_comment.delete()
    return redirect('main:showpost',post_id)