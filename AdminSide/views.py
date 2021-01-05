from django.shortcuts import render
from .models import Cliente
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView )



class ClientListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'AdminSide/AdminView.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'clientList'
    paginate_by = 12


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Cliente

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ['name', 'edad', 'asolea']

class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ['name', 'edad', 'asolea']

class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = '/karen/'
