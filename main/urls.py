from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('messages/', views.messages_list, name='messages_list'),
    path('about/', views.about, name='about'),  
]
