from django.shortcuts import render, redirect,reverse
from .models import Filme, Usuario
from .forms import CriarContaForm, FormHomepage
from django.views.generic import TemplateView, ListView, DetailView, FormView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin # classe para bloquear a class base view


# Create your views here.

#def homepage(request):
 #   return render(request, "homepage.html")

# class BaseView é uma classe pra casa view
class Homepage(FormView): # o objetivo exibir um template e formulário
    template_name = "homepage.html"
    form_class = FormHomepage

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated: # Usuário esta autenticado:
            # redireciona para a homefilmes
            return redirect('filme:homefilmes')
        else:
             return super().get(request, *args, **kwargs) # redireciona para a homepage


    def get_success_url(self):
        email = self.request.POST.get("email")
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')




# url - view - html
# pega as infomações no banco
# def homefilmes(request): (  NA FUNÇÃO BASE VIEW VOCÊ GERÊNCIA TUDO.)
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#     return render(request, "homefilmes.html", context)

class Homefilmes(LoginRequiredMixin, ListView): # ( CLASS BASE VIEW JÁ VEM COM COISAS PRONTAS)
    template_name = "homefilmes.html"
    model = Filme
    # objetc_list -> Lista de intens do modelo


class Detalhesfilme(LoginRequiredMixin, DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
# faz um filtro no banco pro modelo e passa pro html uma variável chamada object que é um item do banco um filme que tem filmes/<int:pk>
# object -> é um item no nosso modelo.


    def get(self, request, *args, **kwargs):
        # descobrir qual o filme ele ta acessando
        # somar 1 nas visualizações daquele filme
        # salvar
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs) # redireciona o usuário para a url final


# editar uma função , passar uma variável para um View especifica
    def get_context_data(self, **kwargs):
        # context é um dicionário que contém todas as variáveis que a pagina html consegue acessar.
        context = super(Detalhesfilme,self).get_context_data(**kwargs)
        # filtrar a minha tabela de filmes pegando os filmes cuja categoria é igual a categoria do filme da página(object)
       # self.get_object() pega o objeto dentro da view
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5] # é uma lista python
        context["filmes_relacionados"] = filmes_relacionados # o nome da variável é a chave do dicionário.
        return context


class Pesquisafilme(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Filme


# está editando o object_list
    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None


#  UpdateView classe que passa o formulário para o usuário e precisa da definição def get_success_url(self):
class Paginaperfil(LoginRequiredMixin, UpdateView):
    template_name = "editarperfil.html"
    model = Usuario
    fields = ['first_name', 'last_name', 'email']
# depois de editar o perfil e direcionado para homefilmes
    def get_success_url(self):
        return reverse('filme:homefilmes')


class Criarconta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm  # ta criando um item no banco

    def form_valid(self, form):
        form.save() # salva o formulário no banco
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('filme:login') # esta retornando o link que corresponde ao link do filme login o texto do link