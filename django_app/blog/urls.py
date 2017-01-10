from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^$', views.blog),
    url(r'^part2/layout1/', views.part2_layout1),
    url(r'^part2/prob1/', views.prob1),
]
