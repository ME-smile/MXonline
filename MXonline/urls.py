"""MXonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.views.static import serve

import xadmin

from . import views
from MXonline.settings import MEDIA_ROOT
from users.views import LoginView,RegisterView,ActiveUserView,ForgetPwdView,ResetPwdView,ModifyPwdView

from organization.views import OrgView

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('',views.index,name='index'),
    path('login/',LoginView.as_view(),name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('captcha/',include('captcha.urls')),
    path('active/<str:active_code>',ActiveUserView.as_view(),name='active_code'),
    path('forget/',ForgetPwdView.as_view(),name='forget_pwd'),
    path('reset/<str:active_code>',ResetPwdView.as_view(),name='reset_pwd'),
    path('modifypw/',ModifyPwdView.as_view(),name='modify_pwd'),
    path('org_list/',OrgView.as_view(),name='org_list'),
    re_path(r'^media/(?P<path>.*)$',serve,{'document_root':MEDIA_ROOT}),
]
