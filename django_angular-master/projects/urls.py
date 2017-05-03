from django.conf.urls import url
from projects import views

urlpatterns = [
    url(r'^projects/user/(?P<pk>[0-9]+)/$', views.project_list),
    url(r'^projects/(?P<pk>[0-9]+)/$', views.project_detail),
    url(r'^questionset/(?P<pk>[0-9]+)/$', views.questionset_detail),
]
