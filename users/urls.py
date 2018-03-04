from django.conf.urls import url
from . import views as users_views

urlpatterns = [
    url(r'^$', users_views.index, name='index'),
    url(r'^signup/$', users_views.signup, name='signup'),
]