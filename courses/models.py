from django.db import models


###课程
class Course(models.Model):
    course_name=models.CharField(max_length=50,verbose_name='课程名称')
    course_img=models.ImageField(max_length=100,upload_to='Banner/%Y/%m',verbose_name='课程图片')
    course_desc=models.CharField(max_length=200,null=True,verbose_name='课程描述')
    course_details=models.TextField(verbose_name='课程详情')
    course_degree=models.CharField(max_length=10,null=True,choices=(('low_rank','初级'),('middle_rank','中级'),('high_rank','高级')),verbose_name='难度')
    course_duration=models.IntegerField(default=0,verbose_name='课程时长')
    course_created_time=models.DateTimeField(auto_now_add=True,null=True,verbose_name='创建时间')
    learning_nums=models.IntegerField(default=0,verbose_name='学习人数')
    favor_nums=models.IntegerField(default=0,verbose_name='收藏人数')
    click_nums=models.IntegerField(default=0,verbose_name='点击量')

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name='课程'
        verbose_name_plural=verbose_name

###章节
class Section(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='课程')
    section_name=models.CharField(max_length=20,verbose_name='章节名称')
    section_created_time=models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

    def __str__(self):
        return self.section_name

    class Meta:
        verbose_name='章节'
        verbose_name_plural=verbose_name

###视频
class Vedio(models.Model):
    section=models.ForeignKey(Section,on_delete=models.CASCADE,verbose_name='章节')
    vedio_name=models.CharField(max_length=50,verbose_name='视频名称')
    vedio_created_time=models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    
    def __str__(self):
        return self.section_name

    class Meta:
        verbose_name='视频'
        verbose_name_plural=verbose_name

class CourseResource(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='课程')
    resource_name=models.CharField(max_length=100,verbose_name='资源名称')
    resource_created_time=models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    download=models.FileField(upload_to='course/resource/%Y/%m',verbose_name='下载资源')

    class Meta:
        verbose_name='资源'
        verbose_name_plural=verbose_name



