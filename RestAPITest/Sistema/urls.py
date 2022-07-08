from django.urls import URLPattern, path
from .views import SistemaDetailVista, SistemaListaVista

urlpatterns = [
    path('company/',SistemaListaVista.as_view(), name='sistema_lista'),
    path('company/<int:id>/',SistemaDetailVista.as_view(),name='Company'),
]