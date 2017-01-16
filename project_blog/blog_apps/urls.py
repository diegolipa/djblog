"""project_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from blog_apps import views
from .views import Home

urlpatterns = [
	url(r'^$', Home.as_view(), name="home"),
	url(r'^post/list$', views.PostList.as_view(), name='post_list'),
	url(r'^post/new$', views.PostCreate.as_view(), name='post_new'),
	url(r'^post/edit/(?P<pk>\d+)$', views.PostUpdate.as_view(), name='post_edit'),
	url(r'^post/delete/(?P<pk>\d+)$', views.PostDelete.as_view(), name='post_delete'),

	url(r'^comment/list$', views.commentary_list, name='commentary_list'),
	url(r'^comment/new$', views.commentay_create, name='commentay_new'),
	url(r'^comment/edit/(?P<pk>\d+)$', views.commentary_update, name='commentary_edit'),
	url(r'^comment/delete/(?P<pk>\d+)$', views.commentary_delete, name='commentary_delete'),

]
