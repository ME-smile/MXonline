# Generated by Django 2.1.3 on 2018-11-21 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_courseorg_org_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='course_nums',
            field=models.IntegerField(default=0, verbose_name='课程数'),
        ),
        migrations.AddField(
            model_name='courseorg',
            name='stu_nums',
            field=models.IntegerField(default=0, verbose_name='学习人数'),
        ),
    ]
