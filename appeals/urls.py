from xml.dom.minidom import Document

from django.urls import path

from .views import home

urlpatterns = [
    path('', home, name='home'),
] 