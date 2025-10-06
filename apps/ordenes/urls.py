from django.urls import path
from . import views

app_name = 'ordenes'

urlpatterns = [   
    path('mesas/', views.MesaListView.as_view(), name='mesa_list'), 
    path('mesas/add/', views.MesaCreateView.as_view(), name='mesas_create'),
    path('mesas/<int:pk>/edit/', views.MesaUpdateView.as_view(), name='mesas_update'),
    path('mesas/<int:pk>/delete/', views.MesaDeleteView.as_view(), name='mesas_delete'),
    path('estados/', views.MesaEstadoListView.as_view(), name='estado_list'),
    path('estados/add/', views.MesaEstadoCreateView.as_view(), name='estado_create'),
    path('estados/<int:pk>/edit/', views.MesaEstadoUpdateView.as_view(), name='estado_update'),
    path('estados/<int:pk>/delete/', views.MesaEstadoDeleteView.as_view(), name='estado_delete'),
]