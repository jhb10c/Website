from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
     path('teaching/', views.teaching, name='teaching'),
    path('research/', views.research, name='research'),
    path('3dprinting/', views.dprinting, name='dprinting'),
    path('seminars/', views.seminars, name='seminars'),
]
