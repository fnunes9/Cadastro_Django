from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    #enviando os dados da tela ao db
    novo_usuario=Usuario()
    novo_usuario.nome=request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    #exibir os usuários cadastrados 
    usuarios={
        'usuarios': Usuario.objects.all()
    }

    #retornar os dados para a página html
    return render(request,'usuarios/usuarios.html', usuarios)