from django.urls import path
from . import views

urlpatterns = [
    #Pahts del Service
    path('', views.services, name= "services"),
]

