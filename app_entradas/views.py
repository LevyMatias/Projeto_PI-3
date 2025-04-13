from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Entradas
from .forms import EntradasForm

# Create your views here.

class EntradasListView(ListView):
    model = Entradas
    template_name = 'app_entradas/entradas_list.html'
    context_object_name = 'entradas'
    paginate_by = 10
    ordering = ['-data_entrada']

class EntradasDetailView(DetailView):
    model = Entradas
    template_name = 'app_entradas/entradas_detail.html'
    context_object_name = 'entrada'

class EntradasCreateView(LoginRequiredMixin, CreateView):
    model = Entradas
    form_class = EntradasForm
    template_name = 'app_entradas/entradas_form.html'
    success_url = reverse_lazy('entrada-list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Entrada registrada com sucesso!')
        return super().form_valid(form)

class EntradasUpdateView(LoginRequiredMixin, UpdateView):
    model = Entradas
    form_class = EntradasForm
    template_name = 'app_entradas/entradas_form.html'
    context_object_name = 'entrada'
    
    def get_success_url(self):
        return reverse_lazy('entrada-detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        messages.success(self.request, 'Entrada atualizada com sucesso!')
        return super().form_valid(form)

class EntradasDeleteView(LoginRequiredMixin, DeleteView):
    model = Entradas
    template_name = 'app_entradas/entradas_confirm_delete.html'
    success_url = reverse_lazy('entrada-list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Entrada excluída com sucesso!')
        return super().delete(request, *args, **kwargs)

@login_required
def entradas_list(request):
    entradas = Entradas.objects.all().order_by('-data_entrada')
    return render(request, 'app_entradas/entradas_list.html', {'entradas': entradas})
