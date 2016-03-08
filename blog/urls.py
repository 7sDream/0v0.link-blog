from django.conf.urls import url

from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^(?:index/)?$', views.index, name='index'),
    url(r'^index/(?P<page>\d+)/$', views.index, name='index-with-page'),

    url(r'^post/(?P<slug>[\w-]+)/$', views.post, name='post'),

    url(r'^category/(?P<slug>[\w-]+)/$', views.category, name='category'),
    url(r'^category/(?P<slug>[\w-]+)/(?P<page>\d+)/$', views.category,
        name='category-with-page'),

    url(r'^tag/(?P<slug>[\w-]+)$', views.tag, name='tag'),
    url(r'^tag/(?P<slug>[\w-]+)/(?P<page>\d+)/$', views.tag,
        name='tag-with-page'),

    url(r'^search/$', view=views.search, name='search'),

    url(r'^share/(?P<slug>[\w-]+)/$', views.share, name='share')
]
