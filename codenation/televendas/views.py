from rest_framework import viewsets
from televendas.serializers import PlanoComissoesSerializer, VendaSerializer, VendedorSerializer
from .models import PlanoComissoes, Venda, Vendedor


class PlanoComissoesViewSet(viewsets.ModelViewSet):
    queryset = PlanoComissoes.objects.all()
    serializer_class = PlanoComissoesSerializer

class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer

class VendaViewSet(viewsets.ModelViewSet):    
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
