
from django.urls import path
from app_cad_user import views

urlpatterns = [
    #rota, view responsável, nome de referência
    #usuarios.com
    path('',views.home,name='home'),
    #usuarios.com/usuarios
    path('usuarios', view.usuarios, name='listagen_usuarios')
]
