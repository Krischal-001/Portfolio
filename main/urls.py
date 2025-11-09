from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Your main portfolio view
    # add other app routes here
]
