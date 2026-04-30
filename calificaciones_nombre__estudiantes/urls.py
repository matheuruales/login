"""Rutas de autenticacion y vista base protegida."""

from django.contrib.auth import views as auth_views
from django.urls import path

from .forms import InicioSesionForm
from .views import (
    RegistroUsuarioView,
    crear_calificacion,
    editar_calificacion,
    eliminar_calificacion,
    listar_calificaciones,
    promedio_general,
)


urlpatterns = [
    path("", listar_calificaciones, name="listar"),
    path("crear/", crear_calificacion, name="crear_calificacion"),
    path("editar/<int:pk>/", editar_calificacion, name="editar_calificacion"),
    path("eliminar/<int:pk>/", eliminar_calificacion, name="eliminar_calificacion"),
    path("promedio-general/", promedio_general, name="promedio_general"),
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
