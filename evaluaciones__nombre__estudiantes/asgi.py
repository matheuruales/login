"""Configuracion ASGI del proyecto evaluaciones__nombre__estudiantes."""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "evaluaciones__nombre__estudiantes.settings",
)

application = get_asgi_application()
