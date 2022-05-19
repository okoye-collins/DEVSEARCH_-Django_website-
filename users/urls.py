from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='signup'),


    path('', views.profile, name='profile'),
    path('user_profile/<str:pk>/', views.userprofile, name='user_profile'),
] 