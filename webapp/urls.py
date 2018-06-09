from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mainpage, name='main_page'),
    url(r'^add/$', views.add, name='add'),
    url(r'(?P<pk>\d+)/edit/$', views.edit, name='edit')
]