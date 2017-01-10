from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^$', views.blog, name='blog'),
    url(r'^part2/layout1/', views.part2_layout1, name='layout1'),
]
