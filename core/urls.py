from django.conf.urls import patterns, include, url
from core.views import class_list, altar_list, children_going_to_year_7

urlpatterns = [
    url(r'^class/(?P<name>\d+&?\d?)/', class_list),
    url(r'^altar-list/', altar_list),
    url(r'^children-going-to-year-7/', children_going_to_year_7),
]
