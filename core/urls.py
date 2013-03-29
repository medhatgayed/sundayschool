from django.conf.urls import patterns, include, url

urlpatterns = patterns('core.views',
    url(r'^class/(?P<name>\d+&?\d?)/', 'class_list'),
)