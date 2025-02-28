from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

from . models import RegistroModel, IPModel

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput



# ------- Gerente ------- #



class CriarGerente(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    username = forms.CharField(

        label = "Nome de usuário",
        
        help_text = " ",

    )

    password1 = forms.CharField(

        label = "Senha",

        help_text = """
        
        &nbsp
        <ul class="form-text text-muted">

            <li>Sua senha não deve conter dados pessoais.</li>
            <li>Sua senha não pode ser uma senha comum.</li>
            <li>Sua senha deve conter 8 caracteres ou mais.</li>
            <li>Sua senha não pode conter apenas números.</li>

        </ul>

        """,
    )

    password2 = forms.CharField(

        label= "Repita a sua senha",  

        help_text = " ",

    )

class Login(AuthenticationForm):

    username = forms.CharField()
    password = forms.CharField(widget=PasswordInput())

