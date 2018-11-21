from django.shortcuts import render
from django.views import View
from pure_pagination import Paginator,EmptyPage,PageNotAnInteger


from .models import CourseOrg,CityDict
# Create your views here.
class OrgView(View):
    def get(self,request):
        all_orgs=CourseOrg.objects.all()
        hot_orgs=all_orgs.order_by('-click_nums')[:3]
        all_cities=CityDict.objects.all()
        

        city_id=request.GET.get('city','')
        category=request.GET.get('ct','')
        sort=request.GET.get('sort','')

        if city_id:
            all_orgs=CourseOrg.objects.filter(city_id=int(city_id))

       
        
        if category:
            all_orgs=CourseOrg.objects.filter(org_category=category)

        if sort:
            if sort == 'stu_nums':
                all_orgs=all_orgs.order_by('-stu_nums')
            elif sort == 'course_nums':
                all_orgs=all_orgs.order_by('-course_nums')
        try:
            page=request.GET.get('page',1)
        except PageNotAnInteger:
            page=1

        org_nums=all_orgs.count()
        p=Paginator(all_orgs,3,request=request)
        
        orgs=p.page(page)
        return render(request,'org-list.html',{
            'all_orgs':orgs,
            'all_cities':all_cities,
            'org_nums':org_nums,
            'city_id':city_id,
            'category':category,
            'hot_orgs':hot_orgs,
            'sort':sort,
        })