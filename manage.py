#!/usr/bin/env python
"""Utilidad de linea de comandos para tareas administrativas de Django."""
import os
import sys


def main():
    """Ejecuta las tareas administrativas del proyecto."""
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "evaluaciones__nombre__estudiantes.settings",
    )
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. Verifica que este instalado y que "
            "el entorno virtual se encuentre activado."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
