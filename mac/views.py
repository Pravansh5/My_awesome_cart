from django.http import HttpResponse
from django.shortcuts import render 
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

def index(request):
   
    return render(request, 'index.html',)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # password2 = request.POST.get('password2')
        email = request.POST.get('GMAIL')

        # Create the user
        if User.objects.filter(username=username).exists():
            # Handle username already exists error
            messages.error(request,'user already exist!!')
            return redirect('/admin/login')
        if User.objects.filter(email=email).exists():
            # Handle username already exists error
            messages.error(request,'user already exist!!')
            return redirect('/admin/login')
        
        print(username)
        print(password)
        print(email)
        user = User.objects.create_superuser(username=username, password=password, email=email)
        user.save()
        # You can also perform additional steps like sending a confirmation email, etc.
        messages.error(request,'User registered successfully')
        return redirect('/admin/login')

    return render(request, 'register.html')
