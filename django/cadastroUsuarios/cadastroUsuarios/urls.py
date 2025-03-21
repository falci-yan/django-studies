from django.urls import include, path
from cadastro import views

urlpatterns = [
    path('', views.home, name='home'),
    path('usuarios/', views.cadastra_usuarios, name='listagem_usuarios'),
]
