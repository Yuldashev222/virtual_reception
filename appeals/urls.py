from xml.dom.minidom import Document

from django.urls import path

from .views import home, post_appeal, test

urlpatterns = [
    path('', home, name='home'),
    path('post-appeal/', post_appeal, name='post-appeal'),
    path('test/', test, name='test'),
]