from django.db import models

from users.models import User
from courses.models import Course

# class UserOperations(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,verbose_name='用户')
#     course = models.ForeignKey(Course,null=True,verbose_name='课程')

#     class Meta:
#         abstract = True


class UserConsult(models.Model):
# class UserConsult(UserOperations):
    username = models.CharField(max_length=20,null=True,verbose_name="姓名")
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户')
    tel_number = models.CharField(max_length=11,null=True,verbose_name="手机")
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='课程')
    course_name = models.CharField(max_length=50,null=True,verbose_name="课程名")
    consulted_time=models.DateTimeField(auto_now_add=True,verbose_name='咨询时间')

    class Meta:
        verbose_name='用户咨询'
        verbose_name_plural=verbose_name



###课程评论
class CourseComment(models.Model):
# class CourseComment(UserOperations):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="用户")
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name="课程")
    comments_content=models.CharField(max_length=200,verbose_name='用户评论')
    comments_created_time=models.DateTimeField(auto_now_add=True,verbose_name='评论时间')

    class Meta:
            verbose_name='课程评论'
            verbose_name_plural=verbose_name

###用户课程
class UserCourse(models.Model):
# class UserCourse(UserOperations):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="用户")
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name="课程")
    start_learing_time=models.DateTimeField(auto_now_add=True,verbose_name='开始学习时间')

    class Meta:
        verbose_name='用户课程'
        verbose_name_plural=verbose_name


###用户收藏
class UserFavor(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户')
    favor_id=models.IntegerField(default=0,verbose_name='数据ID')
    favor_type=models.IntegerField(default=1,choices=((1,'课程'),(2,'讲师'),(3,'机构')))
    favor_created_time=models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name='用户收藏'
            verbose_name_plural=verbose_name




###用户消息
class UserMessage(models.Model):
    # user=models.IntegerField(default=0,verbose_name='接受用户')
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户')
    message=models.CharField(max_length=500,null=True,verbose_name='消息内容')
    message_send_time=models.DateTimeField(auto_now_add=True,verbose_name='发送时间')
    has_read=models.BooleanField(default=False,verbose_name='是否已读')

    class Meta:
        verbose_name='用户消息'
        verbose_name_plural=verbose_name



