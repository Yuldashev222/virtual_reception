from django.urls import path

from .views import *

urlpatterns = [
    # path('test/', test),
    path('profile/<str:username>/', profile, name='profile'),
    path('add-admin/', add_admin, name='add-admin'),
    path('logout/<str:username>/', logout_admin, name='logout'),
    path('login/', admin_login, name='login'),
    path('', dashboard, name='dashboard')
]

