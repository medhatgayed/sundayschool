# Create your views here.
from core.models import Child, SundaySchoolClass
from django.shortcuts import render

def class_list(request, name):
    sunday_school_class = SundaySchoolClass.objects.get(name=name)
    return render(request, 'core/class_list.html', {'sunday_school_class': sunday_school_class})
    

def altar_list(request):
    sunday_school_classes = SundaySchoolClass.objects.all()
    return render(request, 'core/altar_list.html', {'sunday_school_classes': sunday_school_classes})
