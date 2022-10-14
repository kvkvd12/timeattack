from django.shortcuts import render, redirect
from .models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        User.objects.create_user(username=username, password=password, phone=phone, address=address)
        print(username,password,phone,address)
        
        
        return redirect('/login')
    
def login(request):
    if request.method == "GET":
        user = request.user.is_authenticated
        
        if user:
            return redirect('/home')
        else:
            return render(request, 'login.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        me = auth.authenticate(request, username=username, password=password)
        
        if me is not None:
            auth.login(request, me)
            
            return redirect('/login')


def home(request):
    user = request.user.is_authenticated
    
    if user:
        return redirect('/home')
    else:
        return redirect('/login')
    
