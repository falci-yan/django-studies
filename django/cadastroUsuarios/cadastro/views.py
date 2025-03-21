from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def cadastra_usuarios(request):

    novo_usuario = cadastra_usuarios()
    novo_usuario.nome = request.POST('campo_nome')
    novo_usuario.idade = request.POST('campo_idade')
    novo_usuario.save()

    usuarios={
        'usuarios': cadastra_usuarios.objects.all()
    }

    #Retornar os dados para a página de listagem de usuários
    return render(request, 'lista_usuarios.html', cadastra_usuarios)