from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^index.html$', views.post_list, name='index'),
    url(r'^login.html[#]?$', views.login, name='login'),
    url(r'^register.html[#]?$', views.register, name='register'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^post/(?P<hash_name>[a-zA-Z0-9_]+)$', views.post, name='post'),
    url(r'^result/(?P<hash_name>^#\w+)/$', views.result, name='result'),
    url(r'^search$', views.search, name='search'),
    url(r'^base.html$', views.base, name='base'),
	url(r'^login_redirect$', views.login_redirect, name='login_redirect'),
]
