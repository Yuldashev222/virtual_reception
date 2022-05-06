from django.urls import path

from .views import *

urlpatterns = [
    # path('test/', test),
    path('', admin_login, name='login'),
    path('appeals/<int:id>/', single_appeal, name='single-appeal'),
    path('appeals/', appeals, name='appeals'),
    path('answers/', answers, name='answers'),
    path('send-answer/', send_answer, name='send-answer'),
    path('applicants-view/', applicants_view, name='applicants-view'),
    path('chat/', chat, name='chat'),
    path('profile/<str:username>/', profile, name='profile'),
    path('add-admin/', add_admin, name='add-admin'),
    path('logout/<str:username>/', logout_admin, name='logout'),
    path('appeals/download-appealfile/<int:id>/', download_appealFile, name='download-appealFile'),
    path('answers/download-answerFile/<int:id>/', download_answerFile, name='download-answerFile'),
    path('<str:username>/', dashboard, name='dashboard'),
]
