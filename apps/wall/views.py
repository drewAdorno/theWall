from django.shortcuts import render, redirect
from . models import *
from .. app1.models import User

def index(request):
    
    context={
        'messages':Message.objects.all().order_by("-created_at"),
        'comments':Comment.objects.all().order_by("-updated_at")
    }
    return render(request, 'wall/index.html', context)

def post_message(request):
    Message.objects.create(message=request.POST['message'], poster=User.objects.get(id=request.session['loggedInUser_id']))
    return redirect('/wall')

def post_comment(request, message_id):
    Comment.objects.create(comment=request.POST['comment'], poster=User.objects.get(id=request.session['loggedInUser_id']), message=Message.objects.get(id=message_id))
    return redirect('/wall')
