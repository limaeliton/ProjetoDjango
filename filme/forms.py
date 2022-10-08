
# FORMULÁRIOS PERSONALIZADOS
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms


# formulário padrão do Django
class FormHomepage(forms.Form):
    email = forms.EmailField(label=False)


# cria um usuário no banco de dados
# formulário de criação do usuário
class CriarContaForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2') # campos obrigatórios





