from django.db import models

class User(models.Model):
    username=models.CharField(max_length=20,verbose_name='用户名')
    nick_name=models.CharField(max_length=50,verbose_name='昵称',null=True)
    birthday=models.DateField(verbose_name='生日',null=True,blank=True)
    gender=models.CharField(choices=(('male','男'),('female','女')),max_length=6,default='女')
    address=models.CharField(max_length=100,null=True)
    tel_number=models.CharField(max_length=11,null=True,blank=True)
    image=models.ImageField(upload_to='image/%Y/%m',default='image/default.png',max_length=100)
    

    def __str__(self):
        return self.username

    class Meta:
        verbose_name='用户'
        verbose_name_plural=verbose_name

class EmailVerifyReord(models.Model):
    code=models.CharField(max_length=20,verbose_name='验证码')
    email=models.EmailField(max_length=50,verbose_name='邮箱')
    send_type=models.CharField(choices=(('register','注册'),('find_back_pwd','找回密码')),max_length=20,verbose_name='邮件类型')
    send_time=models.DateTimeField(auto_now_add=True,verbose_name='发送时间 ')

    class Meta:
        verbose_name='邮箱验证码'
        verbose_name_plural=verbose_name
        
class Banner(models.Model):
    title=models.CharField(max_length=50,verbose_name='标题')
    img=models.ImageField(max_length=100,upload_to='Banner/%Y/%m',verbose_name='轮播图')
    url=models.URLField(max_length=200,verbose_name='访问地址')
    index=models.IntegerField(default=100,verbose_name='顺序')
    add_time=models.DateTimeField(auto_now=True,verbose_name='添加时间')

    class Meta:
            verbose_name='轮播图'
            verbose_name_plural=verbose_name
        
