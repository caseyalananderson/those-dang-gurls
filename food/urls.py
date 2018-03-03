from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.food_list, name='food_list'),
    url(r'^post/(?P<pk>\d+)/$', views.food_post, name='food_post'),
    url(r'^post/new/$', views.new_food_entry, name='new_food_entry'),
]
