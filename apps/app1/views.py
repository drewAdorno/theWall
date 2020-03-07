from django.shortcuts import render, redirect
from django.contrib import messages
from . models import *
import bcrypt

def validate(request):
    errors=User.objects.validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value)
        return (True)
    return(False)

def index(request):
    if 'loggedInUser' not in request.session:
        request.session['loggedInUser']=""
        return render(request,'app1/index.html')
    elif request.session['loggedInUser']=="":
        return render(request,'app1/index.html')
    return redirect('/success')

def register(request):
    if(validate(request)):                  #if there are any post validation errors redirect with error messaging
        return redirect('/')
    else:
        hashed_pw=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())   #putting hashed pw into db

        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashed_pw, birthday=request.POST['birthday'])

        loggedInUser=User.objects.get(email=request.POST['email'])
        request.session['loggedInUser_name']=loggedInUser.first_name
        request.session['loggedInUser_id']=loggedInUser.id

        return redirect('/success')

def login(request):
    emailFilter=User.objects.filter(email=request.POST['email'])
    user=emailFilter[0]

    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        request.session['loggedInUser_name']=user.first_name
        request.session['loggedInUser_id']=user.id
        return redirect('/wall')
    else:
        return redirect('/')

def success(request):
    
    if 'loggedInUser' not in request.session or request.session['loggedInUser_name'] == "":
        return(redirect('/'))
    return redirect('/wall')

def logout(request):
    request.session.clear()
    return redirect('/')