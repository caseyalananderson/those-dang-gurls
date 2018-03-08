from django.conf.urls import url
from . import views

urlpatterns = [

    # Posts
    url(r'^post/$', views.foodpost_list, name='foodpost_list'),
    url(r'^post/(?P<pk>\d+)/$', views.foodpost_detail, name='foodpost_detail'),

    # Recipes
    # url(r'^recipe/$', views.recipe_list, name='recipe_list'),
    url(r'^recipe/(?P<pk>\d+)/$', views.recipe_detail, name='recipe_detail'),

]
