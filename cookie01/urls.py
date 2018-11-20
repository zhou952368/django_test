from django.conf.urls import url

from cookie01 import views

urlpatterns = [
    url('set/', views.cookie01),
    url('get/', views.cookie02),
    url('1/', views.session1),
]
