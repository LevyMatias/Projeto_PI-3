from django.urls import path
from . import views

urlpatterns = [
    path('', views.EntradasListView.as_view(), name='entrada-list'),
    path('<int:pk>/', views.EntradasDetailView.as_view(), name='entrada-detail'),
    path('nova/', views.EntradasCreateView.as_view(), name='entrada-create'),
    path('<int:pk>/editar/', views.EntradasUpdateView.as_view(), name='entrada-update'),
    path('<int:pk>/excluir/', views.EntradasDeleteView.as_view(), name='entrada-delete'),
] 