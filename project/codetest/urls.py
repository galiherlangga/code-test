from django.urls import path

from codetest import views

urlpatterns = [
    path(r'', views.register, name='register'),
    path(r'dashboard', views.dashboard, name='dashboard'),
    path(r'login', views.login, name='login'),
]
