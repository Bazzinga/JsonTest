from django.conf.urls import patterns, include, url
from story.views import IndexView, CategoryListAPIView, CategorysRetrieveAPIView

urlpatterns = patterns('',
     url(r'^$', IndexView.as_view(), name='home'),
     url(r'^api/categorys/$', CategoryListAPIView.as_view(), name='list'),
     url(r'^api/categorys/(?P<pk>\d+)/$', CategorysRetrieveAPIView.as_view(), name='retrieve'),
)
