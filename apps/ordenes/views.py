from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from apps.ordenes.forms import MesaEstadoForm, MesaForm
from apps.ordenes.models import Mesa, MesaEstado

class MesaEstadoListView(LoginRequiredMixin, ListView):
    model = MesaEstado
    template_name = 'mesas/estado_list.html'
    context_object_name = 'estados'
    
class MesaEstadoCreateView(LoginRequiredMixin, CreateView):
    model = MesaEstado
    form_class = MesaEstadoForm
    template_name = 'mesas/estado_form.html'
    success_url = '/ordenes/estados/'
    
class MesaEstadoUpdateView(LoginRequiredMixin, UpdateView):
    model = MesaEstado
    form_class = MesaEstadoForm
    template_name = 'mesas/estado_form.html'
    success_url = '/ordenes/estados/'
    
class MesaEstadoDeleteView(LoginRequiredMixin, DeleteView):
    model = MesaEstado
    template_name = 'mesas/estado_confirm_delete.html'
    success_url = '/ordenes/estados/'


class MesaListView(LoginRequiredMixin, ListView):
    model = Mesa
    template_name = 'mesas/mesa_list.html'
    context_object_name = 'mesas'

class MesaCreateView(LoginRequiredMixin, CreateView):
    model = Mesa
    form_class = MesaForm
    template_name = 'mesas/mesa_form.html'
    success_url = '/ordenes/mesas/'
    
class MesaUpdateView(LoginRequiredMixin, UpdateView):
    model = Mesa
    form_class = MesaForm
    template_name = 'mesas/mesa_form.html'
    success_url = '/ordenes/mesas/'
    
class MesaDeleteView(LoginRequiredMixin, DeleteView):
    model = Mesa
    template_name = 'mesas/mesa_confirm_delete.html'
    success_url = '/ordenes/mesas/'

