# url - view - template
from django.urls import path, reverse_lazy
from .views import Homepage, Homefilmes, Detalhesfilme, Pesquisafilme, Paginaperfil, Criarconta
from django.contrib.auth import views as auth_view # VIEW DE AUTENTICAÇÃO

# faz referência PARA A PASTA hashflix URLS.PY
app_name = 'filme'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    #filmes/<int:pk> pega o filme pela chave primária do model da classe.
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name='detalhesfilme'), # a VIEW consegue conversar com a URL de uma forma Dinámica
    path('pesquisa/', Pesquisafilme.as_view(), name='pesquisafilme'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'), # é uma classe que já vem pronta com um formulário de login do usuário
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarperfil/<int:pk>',Paginaperfil.as_view(), name='editarperfil'),
    path('criarconta/', Criarconta.as_view(), name='criarconta'),
    path('mudarsenha/', auth_view.PasswordChangeView.as_view(template_name='editarperfil.html',
                                                                success_url=reverse_lazy('filme:homefilmes')),name='mudarsenha'), # .as_view é uma classe


]