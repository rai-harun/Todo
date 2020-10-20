from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('createnote/', views.createNote, name='createnote'),
    path('updatenote/<str:pk>/', views.updateNote, name='updatenote'),
    path('deletenote/<str:pk>/', views.deleteNote, name='deletenote'),
]