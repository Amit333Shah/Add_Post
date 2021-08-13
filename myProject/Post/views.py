from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from.models import PostText
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from.forms import PostTextForm


# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if username=="":
            messages.info(request,"please enter username")
            return redirect('register')
        elif email=="":
            messages.info(request,"please enter email")
            return redirect('register')    
        elif password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email alredy Taken")
                return redirect("register")
   
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save()
                print("user create")
                return redirect('login')
        else:
            print("password not matched")   
            return redirect('register')
    else:
        return render(request,'register.html')      

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        users=auth.authenticate(username=username,password=password)
        if users is not None:
            auth.login(request,users)
            return redirect('/show')
        else:
            messages.info(request,"invalide creadints")
            print("wrong input")
            return redirect('login')
    else:
        return render(request,'login.html')        
def logout(request):
    auth.logout(request)
    return redirect('/')     
@login_required
def postShow(request):
    user=request.user
    # if user is not auth.authenticate:
    #     return redirect("login")

    # else:    
    #     posts=PostText.objects.filter(user=user)
    #     return render(request,"postShow.html",{'posts':posts})  
    posts=PostText.objects.filter(user=user)
    return render(request,"postShow.html",{'posts':posts})    
@login_required
def postCreate(request):
    post=PostText.objects.all()
    if request.method=="POST":
        user=request.user
        text=request.POST['text']
        texts=PostText(text=text,user=user)
        texts.save()
        return redirect('postShow')
    else:
        return render(request,"postCreate.html")    
@login_required
def destroy(request, id):  
    post = PostText.objects.get(id=id)  
    post.delete()  
    return redirect("/show")  

@login_required
def update(request,id,queryset=None):
    post=PostText.objects.filter(id=id).first()
    form=PostTextForm(request.POST or None,instance=post)
    if form.is_valid():
        form.save()
        return redirect("postShow")
    return render(request,"edit.html",{'form':form})    












