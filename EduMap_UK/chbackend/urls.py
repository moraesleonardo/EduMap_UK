# pylint: disable=no-member
from django.urls import path
from . import views
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name=views.CategoryList.name),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name=views.CategoryDetail.name),
    path('places/', views.PlaceList.as_view(), name=views.PlaceList.name),
    path('places/<int:pk>/', views.PlaceDetail.as_view(), name=views.PlaceDetail.name),
    path('cities/', views.CityList.as_view(), name=views.CityList.name),
    path('api-auth/', include('rest_framework.urls')),
    path('', views.home, name='home'),
]

urlpatterns = format_suffix_patterns(urlpatterns)