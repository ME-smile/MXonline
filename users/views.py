from django.shortcuts import render,redirect,reverse
from django.contrib import auth
from django.contrib.auth.hashers import check_password
from django.views import View
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from users.models import UserProfile
from  .forms import Loginform,RegisterForm

class CustomBackend:
    def authenticate(self,request,username=None,password=None):
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
            else:
                return None
               
            
    def get_user(self,user_id):
        try:
            return UserProfile.objects.get(pk=user_id)
        except UserProfile.DoesNotExist:
            return None

class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm()
        return render(request,'register.html',{'register_form':register_form})


class LoginView(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        login_form = Loginform(request.POST)
        if login_form.is_valid():
            user = CustomBackend().authenticate(request,username=request.POST.get('username',''),password=request.POST.get('password',''))
            if user is not None:
                auth.login(request,user)
                return redirect('index')
            else:
                return render(request,'login.html',{'err_msg':'用户名或密码不正确'})
        else:
            return render(request,'login.html',{'login_form':login_form})     

 
