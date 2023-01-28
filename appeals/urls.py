from xml.dom.minidom import Document

from django.urls import path

from .views import post_appeal, appeals

urlpatterns = [
    path('create/', post_appeal, name='post-appeal'),
    path('', appeals, name='appeals'),
]
