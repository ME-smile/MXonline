import xadmin

from .models import Course,Section,Vedio,CourseResource

class CourseAdmin(object):
    list_display=('course_name','course_degree','course_duration','learning_nums','favor_nums','click_nums')
    search_fields=('course_name','course_degree')
    list_filter=('course_created_time',)
   


class SectionAdmin(object):
    list_display=('course','section_name','section_created_time')
    search_fields=('course__name','section_name')
    list_filter=('section_created_time',)

class VedioAdmin(object):
    list_display=('section','vedio_name','vedio_created_time')
    search_fields=('section__name','vedio_name')
    list_filter=('vedio_created_time',)

class CourseResourceAdmin(object):
    list_display=('course','resource_name','resource_created_time')
    search_fields=('course__name','resource_name',)
    list_filter=('resource_created_time',)
   
xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Section,SectionAdmin)
xadmin.site.register(Vedio,VedioAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)
