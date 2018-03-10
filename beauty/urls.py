from django.conf.urls import url
from . import views

urlpatterns = [

    # Posts
    url(r'^$', views.beautypost_list, name='beautypost_list'),
    url(r'^(?P<pk>\d+)/$', views.beautypost_detail, name='beautypost_detail'),

]
