from django.conf.urls import url

from account import views

urlpatterns = [
    url('login/', views.login, name='login'),
    url('register/', views.register, name='register'),
    url('list/', views.list, name='list')
]
