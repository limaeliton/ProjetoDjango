from django.contrib import admin
from .models import Filme, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin

# só existe porque a gente quer que no admin apareça o campo personalizado filmes_vistos
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico", {'fields': ('filmes_vistos',)})
 )
UserAdmin.fieldsets = tuple(campos)


# Register your models here.
# quando construir uma tabela no banco precisa registrar no ADM
# é um novo Usuário precisa registrar no settings.py  AUTH_USER_MODEL = "filme.Usuario"
admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)
