from django.shortcuts import render, redirect, get_object_or_404
from . impor

from .models import Livro



    
def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros/lista_livros.html', {'livros': livros})


def cadastrar_livro(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        data_public = request.POST.get('data_public')
        descricao = request.POST.get('descricao')
        novo_livro = Livro(titulo=titulo, autor=autor, descricao=descricao, data_public=data_public)
        novo_livro.save()
        
        return redirect('lista_livros') 

    return render(request, 'livros/cadastrar_livro.html')

def deleta_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    livro.delete()
    
    return render (request, 'livros/confirmação.html')


def editar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    if request.method == 'POST':
        livro.titulo = request.POST.get('titulo')
        livro.autor = request.POST.get('autor')
        livro.data_public = request.POST.get('data_public')
        livro.descricao = request.POST.get('descricao')
        livro.save()
        return redirect ('lista_livros')
    return render(request, 'livros/editar_livro.html', {'livro': livro})

