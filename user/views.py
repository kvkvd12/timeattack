from django.shortcuts import render, redirect
from .models import User
from django.contrib import auth


# Create your views here.

def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        User.objects.create_user(username=username, password=password, phone=phone, address=address)
        
        
        return redirect('/login')
    
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
 
        me = auth.authenticate(request, username=username, password=password)
        
        if me is not None:
            auth.login(request, me)
            
            return redirect('/home')
        
        return render(request, 'login.html')

    
def home(request):
    if request.method == 'GET':
        if request.user.is_anonymous:
            return redirect('/login')
        
        return render(request, 'home.html')
    
