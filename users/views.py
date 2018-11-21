from django.shortcuts import render,redirect,reverse
from django.contrib import auth
from django.contrib.auth.hashers import check_password,make_password
from django.views import View
from django.db.models import Q
from django.conf import settings

from users.models import UserProfile,EmailVerifyReord
from  .forms import Loginform,RegisterForm,ForgetPwdForm,ModifyPwdForm
from utils.send_email import send_emails


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

class ActiveUserView(View):
    def get(self,request,active_code):
        #Because the active_code generated at random,there are possible the same record.
        all_records =EmailVerifyReord.objects.filter(code=active_code)

        ## I think it is not proper here....
        if all_records:
            for record in all_records:
                email=record.email
                user=UserProfile.objects.get(email=email)
                user.is_active=True
                user.save()
            return render(request,'login.html')
        else:
            return render(request, 'active_fail.html')

class ForgetPwdView(View):
    def get(self,request):
        forgetpwd_form=ForgetPwdForm()
        return render(request,'forgetpwd.html',{'forgetpwd_form':forgetpwd_form})

    def post(self,request):
        forgetpwd_form=ForgetPwdForm(request.POST)
        if forgetpwd_form.is_valid():
            send_emails(request.POST['email'],'forget_pwd')
            return render(request,'send_email_success.html')
        else:
            return render(request,'forgetpwd.html',{'forgetpwd_form':forgetpwd_form})

class ResetPwdView(View):
    def get(self,request,active_code):

        #Because the active_code generated at random,there are possible the same record.
        all_records =EmailVerifyReord.objects.filter(code=active_code)
        ## I think it is not proper here....
        if all_records:
            for record in all_records:
                email=record.email  
            return render(request,'password_reset.html',{'email':email})
        else:
            return render(request, 'request_reset_pwd_fail')
        return render(request, 'login.html')

   

class ModifyPwdView(View):
    def post(self,request):
        print('进入修改密码函数')
        modifypwd_form =ModifyPwdForm(request.POST)
        email=request.POST['email']
        if modifypwd_form.is_valid():
            if request.POST['password'] != request.POST['confirm_password']:
                return render(request,'password_reset.html',{'email':email,'err_msg':'密码不一致'})
            user = UserProfile.objects.get(email=email)
            user.password=make_password(request.POST['password'])
            user.save()
            return render(request,'login.html')
        else:
            return render(request,'password_reset.html',{'email':email,'modifypwd_form':modifypwd_form})

class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm()
        return render(request,'register.html',{'register_form':register_form})

    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            if UserProfile.objects.filter(email=request.POST['email']):
                return render(request,'register.html',{'err_msg':'该用户已经存在'})
            else:
                user = UserProfile()
                user.username=request.POST['email']
                user.email=user.username
                user.password=make_password(request.POST['password'])
                user.is_active=False
                user.save()

            send_emails(user.email,'register')
            return render(request,'login.html')
        else:
            return render(request,'register.html',{'register_form':register_form})




class LoginView(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        login_form = Loginform(request.POST)
        if login_form.is_valid():
            user = CustomBackend().authenticate(request,username=request.POST.get('username',''),password=request.POST.get('password',''))
            if user is not None:
                if user.is_active:
                    auth.login(request,user)
                    return redirect('index')
                else:
                    return render(request,'login.html',{'err_msg':'用户未激活'})
            else:
                return render(request,'login.html',{'err_msg':'用户名或密码不正确'})
        else:
            return render(request,'login.html',{'login_form':login_form})     

 
