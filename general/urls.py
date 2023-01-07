from django.urls import path

from .views import *

urlpatterns = [
    path('applicants-view/', applicants_view, name='applicants-view'),
    path('<str:username>/', dashboard, name='dashboard'),
    path('', home, name='home')
]
