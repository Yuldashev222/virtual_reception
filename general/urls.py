from django.urls import path

from .views import *

urlpatterns = [
    path('applicants-view/', applicants_view, name='applicants-view'),
    path('', home, name='home')
]
