import xadmin

from .models import UserConsult,UserCourse,UserFavor,CourseComment,UserMessage

# Register your models here.

# class UserConsultAdmin(object):
#     list_display=('user','course','consulted_time')
#     # search_fields=('user__username','course__course_name')
#     list_filter=('consulted_time')

class CourseCommentAdmin(object):
    list_display=('user','course','comments_created_time')


class UserCourseAdmin(object):
    list_display=('user','course','start_learing_time')

# class UserFavorAdmin(object):
#     list_display=('username',)
#     search_fields=('username','tel_number','course_name')
#     list_filter=('username','consulted_time')




class UserMessageAdmin(object):
    list_display=('user','message_send_time','has_read','message')




# xadmin.site.register(UserConsult,UserConsultAdmin)
# xadmin.site.register(UserFavor,UserFavorAdmin)  
xadmin.site.register(CourseComment,CourseCommentAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)
