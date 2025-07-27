from django.shortcuts import render
from .models import User, Post, Notification, Like, Comment
from .admin import userAdmin, postAdmin, notificationAdmin, likeAdmin, commentAdmin

def index(request):
    users=User.objects.all()
    posts=Post.objects.all()
    notifications=Notification.objects.all()
    likes=Like.objects.all()
    comments=Comment.objects.all()
    user_attributes=userAdmin.list_display
    post_attributes=postAdmin.list_display
    notification_attributes=notificationAdmin.list_display
    like_attributes=likeAdmin.list_display
    comment_attributes=commentAdmin.list_display
    query=request.GET.get('query')
    context={
        'users':users,
        'posts':posts,
        'notifications':notifications,
        'likes':likes,
        'comments':comments,
        'user_attributes':user_attributes,
        'post_attributes':post_attributes,
        'notification_attributes':notification_attributes,
        'like_attributes':like_attributes,
        'comment_attributes':comment_attributes,
        'query':query,
    }
    return render(request, 'social_media/index.html',context)