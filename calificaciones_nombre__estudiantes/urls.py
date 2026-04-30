"""Rutas de autenticacion y vista base protegida."""

from django.contrib.auth import views as auth_views
from django.urls import path

from .forms import InicioSesionForm
from .views import RegistroUsuarioView, VistaListarBase


urlpatterns = [
    path("", VistaListarBase.as_view(), name="listar"),
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(
            authentication_form=InicioSesionForm,
            template_name="registration/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
    path(
        "accounts/register/",
        RegistroUsuarioView.as_view(),
        name="register",
    ),
]
