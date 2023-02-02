
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect



# Create your views here.
def login(request):
    if request.method=='POST':
        un=request.POST['username']
        p=request.POST['password1']
        ur=auth.authenticate(username=un,password=p)

        if ur is not None:
            auth.login(request,ur)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        u=request.POST['username']
        fn = request.POST.get('first_name')
        ln = request.POST.get('last_name')
        ema= request.POST.get('email')
        p1= request.POST.get('password1')
        p2= request.POST.get('password2')
        if p1==p2:
            if User.objects.filter(username=u).exists():
                messages.info(request,"Username taken already")
                return redirect('register')
            elif User.objects.filter(email=ema).exists():
                messages.info(request,"Email taken already")
                return redirect('register')
            else:
                user=User.objects.create_user(username=u,first_name=fn,last_name=ln,email=ema,password=p1)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')