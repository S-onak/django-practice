from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignInForm, SignUpForm   # .forms.py 에서 작성한 폼을 불러옴
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method == 'GET':
        form = SignUpForm()
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    
    return render(request, 'accounts/signup.html', {'form': form})

def signin(request):
    if request.method == 'GET':
        form = SignInForm()
    elif request.method == 'POST':
        form = SignInForm(request, data=request.POST)   # 로그인은 유저 검증을 통해 검증 성공, 실패 등의 정보를 반환해야 하기 떄문
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('todos')
            else:
                messages.error(request)
    
    return render(request, 'accounts/signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('signin')