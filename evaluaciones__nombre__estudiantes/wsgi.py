"""Configuracion WSGI del proyecto evaluaciones__nombre__estudiantes."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "evaluaciones__nombre__estudiantes.settings",
)

application = get_wsgi_application()
