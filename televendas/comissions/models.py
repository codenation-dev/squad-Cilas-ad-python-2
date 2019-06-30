from django.db import models

# Create your models here.
class PlanoComissoes(models.Model):
    porcentagem_menor = models.IntegerField()
    valor_minimo = models.FloatField(max_length=20)
    porcentagem_maior = models.IntegerField()
    def __str__(self):
        return 'Plano {} - {}%'.format(self.valor_minimo, self.porcentagem_maior)
    
class Vendedor(models.Model):
    nome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    idade = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    cpf = models.CharField(max_length=30)
    plano_de_comissoes = models.ForeignKey(PlanoComissoes, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class Venda(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    mes = models.CharField(max_length=30)
    valor_vendas = models.FloatField(max_length=20)