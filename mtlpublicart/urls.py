from django.conf.urls import url
from mtlpublicart import views


urlpatterns = [
    url(r'^$', views.index, name='mtl-public-art'),
]
