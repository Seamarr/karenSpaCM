from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from .views import (
    ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView)

urlpatterns = [
    path('', ClientListView.as_view(), name='admin-home'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('client/new/', ClientCreateView.as_view(), name='client-create'),
    path('client/<int:pk>/update/', ClientUpdateView.as_view(), name='client-update'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client-delete'),

]
