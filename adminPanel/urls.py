from django.urls import path

from .views import admin_login, dashboard, appeals

urlpatterns = [
    path('', admin_login, name='login'),
    path('<str:username>', dashboard, name='dashboard'),
    path('appeals/', appeals, name='appeals'),
] 
