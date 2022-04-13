from django.urls import path

from .views import *

urlpatterns = [
    path('', admin_login, name='login'),
    path('appeals/', appeals, name='appeals'),
    path('answers/', answers, name='answers'),
    path('applicants-view/', applicants_view, name='applicants-view'),
    path('chat/', chat, name='chat'),
    path('profile/<str:username>/', profile, name='profile'),
    path('add-admin/', add_admin, name='add-admin'),
    path('logout/<str:username>/', logout_admin, name='logout'),
    path('<str:username>/', dashboard, name='dashboard'),
] 
