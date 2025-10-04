from django.urls import path
from . import views

urlpatterns = [
    path('lista_livros/', views.lista_livros, name='lista_livros'),
    path('cadastrar_livro/', views.cadastrar_livro, name='cadastrar_livro')
]
