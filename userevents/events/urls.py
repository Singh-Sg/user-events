from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^event/new/', views.create_event, name='create_event'),
    url(r'^event/(?P<pk>\d+)/edit/$', views.update_event, name='update_event'),
    url(r'^event/(?P<pk>\d+)/delete/$', views.delete_event, name='delete_event'),
    url(r'^my-event', views.my_events, name='my_events'),
    url(r'^event/join', views.join_event, name='join_event'),
]
