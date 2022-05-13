from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.profile, name='profile'),
    path('user_profile/<str:pk>/', views.userprofile, name='user_profile'),
] 