from django.conf.urls import url
from . import views

urlpatterns = [

    # Posts
    url(r'^$', views.fitnesspost_list, name='fitnesspost_list'),
    url(r'^(?P<pk>\d+)/$', views.fitnesspost_detail, name='fitnesspost_detail'),

]
