from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def usuarios(request):
    #Salvar os dados os dados no banco de dados.
    novo_usuario = usuario()
    novo_usuario.nome = request.POST.get('campo_nome')
    novo_usuario.idade = request.POST.get('campo_idade')

    novo_usuario.save()

    #Exibir todos os usuários cadastrados em uma nova página. O Django espera um dicionário
    usuarios ={
        'usuarios': usuario.objects.all()
    }
    #Retornar os dados para a página de listagem de usuários.
    return render(request, 'lista_usuarios.html', usuarios)
