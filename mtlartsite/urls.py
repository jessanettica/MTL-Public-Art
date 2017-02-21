from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from mtlpublicart import views
from mtlpublicart import views as mtlartviews

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', mtlartviews.logout_page, name='logout'),
    url(r'^register/$', mtlartviews.register_page, name='register'),
    url(r'^montreal_public_art/', include('mtlpublicart.urls')),
]
