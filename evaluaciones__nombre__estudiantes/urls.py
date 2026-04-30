"""Enrutador principal del proyecto."""

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("calificaciones_nombre__estudiantes.urls")),
]
