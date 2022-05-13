from django.urls import path
from . import views

app_name = 'project'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<str:pk>/', views.detail, name='detail'),
    path('add_project/', views.addproject, name='addproject'),
    path('editproject/<str:pk>/', views.updateproject, name='update'),
    path('deleteproject/<str:pk>', views.deleteproject, name='deleteproject'),
]