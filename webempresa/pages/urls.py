from django.urls import path
from . import views

urlpatterns = [
    #Pahts del Blog
    path('<int:page_id>/<slug:page_slug>/',views.page, name='page'),
]

