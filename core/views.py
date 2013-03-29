# Create your views here.
from core.models import Child, SundaySchoolClass
from django.shortcuts import render

def class_list(request, name):
    sunday_school_class = SundaySchoolClass.objects.get(name=name)
    children = sunday_school_class.child_set.all()
    return render(request, 'core/class_list.html', {'sunday_school_class': sunday_school_class,
                                                    'children': children})
    

