from django.urls import path
from .views import answers

urlpatterns = [
    path('', answers, name='answers')
]
