from django.shortcuts import render, redirect,get_object_or_404
from  .models import *
from django.utils import timezone

from django.views.decorators.http import require_POST
from django.http import HttpResponse
import json
from django.contrib.auth.decorators import login_required

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


@require_POST
@login_required
def like_toggle(request,post_id):
    post=get_object_or_404(Post,pk=post_id)
    post_like,post_like_created=Like.objects.get_or_create(user=request.user,post=post)

    if not post_like_created:
        post_like.delete()
        result="like_cancel"

    else:
        result="like"

    context={
        "like_count":post.like_count,
        "result":result
    }

    return HttpResponse(json.dumps(context),content_type="application/json")

@require_POST
@login_required
def dislike_toggle(request,post_id):
    post=get_object_or_404(Post,pk=post_id)
    post_dislike,post_dislike_created=Dislike.objects.get_or_create(user=request.user,post=post)

    if not post_dislike_created:
        post_dislike.delete()
        result="dislike_cancel"
        
    else:
        result="dislike"
    
    context={
        "dislike_count":post.dislike_count,
        "result":result
    }

    return HttpResponse(json.dumps(context),content_type="application/json")
