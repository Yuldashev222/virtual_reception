from django.urls import path

from .views import *

urlpatterns = [
    path('', admin_login, name='login'),
    path('appeals/', appeals, name='appeals'),
    path('answers/', answers, name='answers'),
    path('applicants-view/', applicants_view, name='applicants-view'),
    path('chat/', chat, name='chat'),
    path('<str:username>/', dashboard, name='dashboard'),
] 
