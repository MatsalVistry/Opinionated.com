from django.conf.urls import url
from . import views

app_name = 'politics'

urlpatterns = [
    #/politics/
    url(r'^$', views.IndexView.as_view(), name ='index'),
    
    #/politics/debate id/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    
    
    
    url(r'debate/add/$', views.DebateCreate.as_view(), name = 'debate-add'),


]