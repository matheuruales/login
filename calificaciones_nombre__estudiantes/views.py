from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CalificacionForm, RegistroUsuarioForm
from .models import Calificacion


@login_required
def listar_calificaciones(request):
    """Muestra todas las calificaciones y el promedio general."""

    calificaciones = Calificacion.objects.all().order_by("nombre_estudiante", "asignatura")
    promedio_general = Calificacion.objects.aggregate(promedio_general=Avg("promedio"))[
        "promedio_general"
    ]
    return render(
        request,
        "calificaciones_nombre__estudiantes/listar.html",
        {"calificaciones": calificaciones, "promedio_general": promedio_general},
    )


@login_required
def crear_calificacion(request):
    """Registra una nueva calificacion."""

    if request.method == "POST":
        form = CalificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar")
    else:
        form = CalificacionForm()

    return render(
        request,
        "calificaciones_nombre__estudiantes/crear.html",
        {"form": form},
    )


@login_required
def editar_calificacion(request, pk):
    """Actualiza una calificacion existente."""

    calificacion = get_object_or_404(Calificacion, pk=pk)

    if request.method == "POST":
        form = CalificacionForm(request.POST, instance=calificacion)
        if form.is_valid():
            form.save()
            return redirect("listar")
    else:
        form = CalificacionForm(instance=calificacion)

    return render(
        request,
        "calificaciones_nombre__estudiantes/editar.html",
        {"form": form, "calificacion": calificacion},
    )


@login_required
def eliminar_calificacion(request, pk):
    """Elimina una calificacion previa confirmacion."""

    calificacion = get_object_or_404(Calificacion, pk=pk)
    if request.method == "POST":
        calificacion.delete()
        return redirect("listar")

    return render(
        request,
        "calificaciones_nombre__estudiantes/eliminar.html",
        {"calificacion": calificacion},
    )


@login_required
def promedio_general(request):
    """Muestra el promedio general de todos los registros."""

    promedio = Calificacion.objects.aggregate(promedio_general=Avg("promedio"))[
        "promedio_general"
    ]
    return render(
        request,
        "calificaciones_nombre__estudiantes/promedio_general.html",
        {"promedio_general": promedio},
    )


class RegistroUsuarioView(CreateView):
    """Crea usuarios y los autentica al finalizar el registro."""

    form_class = RegistroUsuarioForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("listar")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("listar")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        login(self.request, self.object)
        return redirect(self.get_success_url())
