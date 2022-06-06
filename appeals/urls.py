from xml.dom.minidom import Document

from django.urls import path

from .views import home, post_appeal

urlpatterns = [
    path('', home, name='home'),
    path('post-appeal/', post_appeal, name='post-appeal'),
]