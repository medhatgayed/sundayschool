from django.conf.urls import url
from core.views import class_list, altar_list, children_in_school_year


urlpatterns = [
    url(r'^class/(?P<name>\d+&?\d?)/', class_list),
    url(r'^altar-list/', altar_list),
    url(r'^children-in-school-year/(?P<school_year>\d{1,2})/', children_in_school_year),
]
