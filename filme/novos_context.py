
# GERÊNCIADOR DE CONTEXT SÃO AS VARIÁVEIS QUE VOCÊ TEM ACESSO DENTRO DO SEU HTML, PERSONALIZADA AQUILO QUE VOCÊ QUER CRIAR

from .models import Filme

def lista_filmes_recentes(request):
    # -data_criacao' para ordenar em ordem decrescente
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:8]
    if lista_filmes:
        filme_destaque = lista_filmes[0]
    else:
        filme_destaque = None
    return {"lista_filmes_recentes": lista_filmes, "filme_destaque": filme_destaque}


def lista_filmes_emalta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:8]
    return {"lista_filmes_emalta" : lista_filmes}


# lembrando que quando e criado um novo conxtet OU FUNÇÃO
# é preciso adicionar no SETTTINGS.PY DO PROJETO no gerênciador de context
