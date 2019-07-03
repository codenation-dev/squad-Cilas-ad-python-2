from django.urls import include, path
from rest_framework import routers
from .views import PlanoComissoesViewSet, VendaViewSet, VendedorViewSet

router = routers.DefaultRouter()
router.register(r'planos-de-comissoes', PlanoComissoesViewSet)
router.register(r'vendedores', VendedorViewSet)
router.register(r'vendas', VendaViewSet)

urlpatterns = [
    path("", include(router.urls))
]

