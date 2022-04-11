from django.urls import path

from .views import admin_login, dashboard, appeals, answers

urlpatterns = [
    path('', admin_login, name='login'),
    path('appeals/', appeals, name='appeals'),
    path('answers/', answers, name='answers'),
    path('<str:username>/', dashboard, name='dashboard'),
] 
