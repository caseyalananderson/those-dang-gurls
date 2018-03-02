from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.food_list, name='index'),
    url(r'^(?P<pk>\d+)/$', views.food_post, name='blog_post')
]
