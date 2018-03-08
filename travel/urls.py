from django.conf.urls import url
from . import views

urlpatterns = [

    # Posts
    url(r'^$', views.travelpost_list, name='travelpost_list'),
    url(r'^(?P<pk>\d+)/$', views.travelpost_detail, name='travelpost_detail'),

]
