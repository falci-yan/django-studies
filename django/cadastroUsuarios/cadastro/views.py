from django.shortcuts import render
from .models import Usuario

# Create your views here.
def home(request):
    return render(request, 'home.html')

def cadastra_usuarios(request):

    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('campo_nome')
    novo_usuario.idade = request.POST.get('campo_idade')
    novo_usuario.save()

    usuarios={
        'usuarios': Usuario.objects.all()
    }

    #Retornar os dados para a página de listagem de usuários
    return render(request, 'lista_usuarios.html', usuarios)