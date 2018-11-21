import xadmin

from .models import CourseOrg,CityDict,Teacher

class CourseOrgAdmin(object):
    list_display=('org_name','org_category','org_address','org_created_time','city','favor_nums','click_nums')
    search_fields=('org_name','org_address','favor_nums')
    list_filter=('org_name','org_address','city')

class CityDictAdmin(object):
    list_display=('city_name','created_time')

class TeacherAdmin(object):
    list_display=('teacher_name','org','work_experience','work_position','teaching_feature','favor_nums','click_nums')
    search_fields=('teacher_name','org__name','teaching_feature','work_experience')
    list_filter=('teacher_name','org','work_experience',)

xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(Teacher,TeacherAdmin)


