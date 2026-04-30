from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import RegistroUsuarioForm


class VistaListarBase(LoginRequiredMixin, TemplateView):
    """Vista inicial protegida para enlazar el resto del proyecto."""

    template_name = "calificaciones_nombre__estudiantes/listar.html"


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
