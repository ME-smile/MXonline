from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from  .models import User
#custom modelBackend to implements loging in by email
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(Q(username=username)|Q(tel_number=tel_number))
            if user.check_password(password):
                return user
        except Exception as e:
                return None

 
# Create your views here.
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(request,username=request.POST.get('username',''),password=request.POST.get('password',''))
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            return render(request,'login.html',{'err_msg':'用户名或密码不正确'})     
    elif request.method == 'GET':
        return render(request,'login.html')

