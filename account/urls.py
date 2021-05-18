from django.urls import path
from .views import register_vendor, register_rider, login_user, logout_user, home

urlpatterns = [
    path('register_vendor/', register_vendor, name='register_vendor'),
    path('register_rider/', register_rider, name='register_rider'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('', home, name='home')
]
