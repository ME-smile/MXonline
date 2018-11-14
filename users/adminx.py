import xadmin
from xadmin import views

from .models import User,EmailVerifyReord,Banner

class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True

class GlobalSetting(object):
    site_title='慕学后台管理系统'
    site_footer='慕学在线网'
    menu_style='accordion'

class UserAdmin(object):
    list_display=('username','nick_name','birthday','gender','address','tel_number')
    search_fields=('username','gender','nick_name')
    list_filter=('birthday','address')


class EmailVerifyReordAdmin(object):
    list_display=('code','email','send_type','send_time')
    search_fields=('code','email')
    list_filter=('send_time',)

class BannerAdmin(object):
    list_display=('title','img','index','add_time','url')
    search_fields=('title','index','url')
    list_filter=('add_time',)

xadmin.site.register(User,UserAdmin)
xadmin.site.register(EmailVerifyReord,EmailVerifyReordAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)