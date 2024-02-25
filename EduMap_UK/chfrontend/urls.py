from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'chfrontend'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('base/', views.base, name='base'),
    path('maps/', views.maps, name='maps'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
