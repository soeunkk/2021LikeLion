from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.validators import validate_email

# Create your views here.
# (참고: 중복체크를 위해선 ajax 비동기 작업이 필요함)
def signup(request):
    if request.method == 'POST':    #case1: 회원가입 폼 완성
        if request.POST['username'] == "" or request.POST['email'] == "" or request.POST['password1'] == "" or request.POST['password2'] == "":  #case1-1: 입력값 누락
            return render(request, 'account/signup.html', {'error':'필수 항목이 입력되지 않았습니다.'})
        elif request.POST['password1'] != request.POST['password2']:  #case1-2: 비밀번호 불일치
            return render(request, 'account/signup.html', {'error':'비밀번호가 일치하지 않습니다.'})
        else:
            try: 
                user = User.objects.get(username=request.POST['username'])   #User 정보에 username이 있는지 확인(case1-3: 아이디 중복)
                return render(request, 'account/signup.html', {'error':'이미 사용 중인 ID입니다.'})
            except User.DoesNotExist:   #case1-4: 계정 생성 가능
                user = User.objects.create_user(
                    request.POST['username'], email=request.POST['email'], password=request.POST['password1']
                )
                auth.login(request, user)
                return redirect('home')
    else:   #case2: 회원가입 화면으로 전환 요청
        return render(request, 'account/signup.html')

def login(request):
    if request.method == 'POST':    #case1: 로그인 폼 완성
        username= request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:    #case1-1: 로그인 성공
            auth.login(request, user)
            return redirect('home')
        else:   #case1-2: 로그인 실패
            return render(request, 'account/login.html', {'error':'ID 또는 비밀번호가 일치하지 않습니다.'})
    else:   #case2: 로그인 화면으로 전환 요청
        return render(request, 'account/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
