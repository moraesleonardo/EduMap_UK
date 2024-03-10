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
<<<<<<< HEAD
    path('cursos/', views.CursoListView.as_view(), name='listar_cursos'),  # Corrigido
    path('cursos/adicionar/', views.CursoCreateView.as_view(), name='adicionar_curso'),
    path('excluir_curso/<int:curso_id>/', views.excluir_curso, name='excluir_curso'),
    
    
=======
>>>>>>> fe5208ff891556a6d785ae0dee2c775a13fb0bed
]
