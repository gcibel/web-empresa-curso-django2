from django.urls import path
from . import views

urlpatterns = [
    #Pahts del Blog
    path('', views.blog, name= "blog"),
    path('category/<int:category_id>/',views.category, name='category'),
]

