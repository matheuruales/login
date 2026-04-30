from decimal import Decimal

from django.test import TestCase

from .models import Calificacion


class CalificacionModelTests(TestCase):
    def test_promedio_se_calcula_automaticamente(self):
        calificacion = Calificacion.objects.create(
            nombre_estudiante="Ana Perez",
            identificacion="12345",
            asignatura="Matematicas",
            nota1=Decimal("3.00"),
            nota2=Decimal("4.00"),
            nota3=Decimal("5.00"),
        )
        self.assertEqual(calificacion.promedio, Decimal("4"))

    def test_obtener_promedio_general_usa_avg(self):
        Calificacion.objects.create(
            nombre_estudiante="Ana Perez",
            identificacion="12345",
            asignatura="Matematicas",
            nota1=Decimal("3.00"),
            nota2=Decimal("4.00"),
            nota3=Decimal("5.00"),
        )
        Calificacion.objects.create(
            nombre_estudiante="Luis Gomez",
            identificacion="67890",
            asignatura="Matematicas",
            nota1=Decimal("1.00"),
            nota2=Decimal("2.00"),
            nota3=Decimal("3.00"),
        )
        promedio_general = Calificacion.obtener_promedio_general()
        self.assertEqual(promedio_general, Decimal("3"))
