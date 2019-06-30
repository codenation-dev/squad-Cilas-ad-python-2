from django.contrib import admin

# Register your models here.
from .models import Vendedor, PlanoComissoes, Venda
admin.site.register([Vendedor, PlanoComissoes, Venda])