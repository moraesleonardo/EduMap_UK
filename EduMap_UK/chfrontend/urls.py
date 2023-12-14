from django.urls import path
from . import views


app_name = 'chfrontend'
urlpatterns = [
    path('', views.placesListMap, name ='placeslist_map'),
    
]