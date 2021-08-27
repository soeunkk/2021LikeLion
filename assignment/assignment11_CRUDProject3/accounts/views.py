from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == "POST":
        try:
            user = User.objects.get(username=request.POST['username'])
            return render(request, 'accounts/signup.html', {'error':"이미 같은 username이 존재합니다."})
        except User.DoesNotExist:
            user = User.objects.create_user(
                request.POST['username'], email=request.POST['email'], password=request.POST['password']
            )
            auth.login(request, user)
            return redirect('home')
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else: 
            return render(request, 'accounts/login.html', {'error':"username 또는 password가 일치하지 않습니다."})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')
    return render(request, 'accounts/signup.html')