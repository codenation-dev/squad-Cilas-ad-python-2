from .models import PlanoComissoes, Venda, Vendedor
from rest_framework import serializers


class PlanoComissoesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlanoComissoes
        fields = ('id', 'url', 'porcentagem_menor', 'valor_minimo', 'porcentagem_maior', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
 
class VendedorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendedor
        fields = ('id', 'nome', 'cep', 'logradouro', 'numero_casa', 'bairro', 'cidade', 'estado', 'telefone', 'data_nascimento', 'email', 'cpf', 'plano_de_comissoes', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
 
class VendaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Venda
        fields = ('id', 'url', 'vendedor', 'valor_vendas', 'valor_comissao', 'mes', 'ano', 'created_at', 'updated_at')
        read_only_fields = ('id', 'valor_comissao', 'created_at', 'updated_at')
 
