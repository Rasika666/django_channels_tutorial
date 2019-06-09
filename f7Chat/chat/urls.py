from . import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]
