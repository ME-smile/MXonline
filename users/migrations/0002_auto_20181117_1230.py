# Generated by Django 2.1.3 on 2018-11-17 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyreord',
            name='send_type',
            field=models.CharField(choices=[('register', '注册'), ('forget_pwd', '忘记密码')], max_length=20, verbose_name='邮件类型'),
        ),
    ]
