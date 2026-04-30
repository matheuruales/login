from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class InicioSesionForm(AuthenticationForm):
    """Formulario de autenticacion con etiquetas en espanol."""

    username = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(
        label="Contrasena",
        strip=False,
        widget=forms.PasswordInput,
    )

    error_messages = {
        "invalid_login": (
            "Usuario o contrasena incorrectos. Verifica los datos e intentalo de nuevo."
        ),
        "inactive": "Esta cuenta se encuentra inactiva.",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"placeholder": "Ingresa tu nombre de usuario"}
        )
        self.fields["password"].widget.attrs.update(
            {"placeholder": "Ingresa tu contrasena"}
        )


class RegistroUsuarioForm(UserCreationForm):
    """Formulario de registro basado en UserCreationForm."""

    email = forms.EmailField(label="Correo electronico", required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Nombre de usuario"
        self.fields["username"].help_text = (
            "Usa hasta 150 caracteres con letras, numeros y simbolos @/./+/-/_."
        )
        self.fields["first_name"].label = "Nombres"
        self.fields["first_name"].required = True
        self.fields["last_name"].label = "Apellidos"
        self.fields["last_name"].required = True
        self.fields["password1"].label = "Contrasena"
        self.fields["password1"].help_text = (
            "La contrasena debe ser segura y cumplir las validaciones de Django."
        )
        self.fields["password2"].label = "Confirmacion de contrasena"
        self.fields["password2"].help_text = "Repite la misma contrasena para confirmarla."

        for nombre_campo in self.fields:
            self.fields[nombre_campo].widget.attrs.setdefault("placeholder", "")

        self.fields["username"].widget.attrs["placeholder"] = "Elige un nombre de usuario"
        self.fields["first_name"].widget.attrs["placeholder"] = "Escribe tus nombres"
        self.fields["last_name"].widget.attrs["placeholder"] = "Escribe tus apellidos"
        self.fields["email"].widget.attrs["placeholder"] = "Escribe tu correo electronico"
        self.fields["password1"].widget.attrs["placeholder"] = "Crea una contrasena"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirma tu contrasena"

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.email = self.cleaned_data["email"]
        usuario.first_name = self.cleaned_data["first_name"]
        usuario.last_name = self.cleaned_data["last_name"]

        if commit:
            usuario.save()

        return usuario
