from django.conf.urls import patterns, include, url
from core.views import class_list, altar_list

urlpatterns = [
    url(r'^class/(?P<name>\d+&?\d?)/', class_list),
    url(r'^altar-list/', altar_list),
]
