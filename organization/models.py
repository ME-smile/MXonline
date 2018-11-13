from django.db import models

class CourseOrg(models.Model):
    org_name=models.CharField(max_length=30,verbose_name='机构名称')
    org_desc=models.TextField(verbose_name='机构描述')
    org_address=models.CharField(max_length=100,verbose_name='机构地址')
    org_img=models.ImageField(max_length=100,upload_to='org/%Y/%m',verbose_name='机构图片')
    org_created_time=models.DateField(auto_now_add=True,verbose_name='创建时间')
    city=models.ForeignKey('CityDict',on_delete=models.CASCADE,verbose_name='所在城市')
    favor_nums=models.IntegerField(default=0,verbose_name='收藏人数')
    click_nums=models.IntegerField(default=0,verbose_name='点击量')

    def __str__(self):
        return self.org_name
    
    class Meta:
        verbose_name='机构'
        verbose_name_plural=verbose_name


class CityDict(models.Model):
    city_name=models.CharField(max_length=20,verbose_name='城市')
    city_desc=models.TextField(verbose_name='描述')
    created_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name='城市'
        verbose_name_plural=verbose_name

class Teacher(models.Model):
    org=models.ForeignKey('CourseOrg',on_delete=models.CASCADE,verbose_name='所属机构')
    teacher_name=models.CharField(max_length=30,verbose_name='机构名称')
    work_experience=models.IntegerField(default=0,verbose_name='工作经验')
    work_company=models.CharField(max_length=50,verbose_name='就职公司')
    work_position=models.CharField(max_length=50,verbose_name='公司职位')
    teaching_feature=models.CharField(max_length=50,verbose_name='教学特点')
    favor_nums=models.IntegerField(default=0,verbose_name='收藏人数')
    click_nums=models.IntegerField(default=0,verbose_name='点击量')
    created_time=models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name='讲师'
            verbose_name_plural=verbose_name
