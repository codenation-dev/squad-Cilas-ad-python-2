from django.db import models
# Model Plano de Comissão
class PlanoComissoes(models.Model):
    porcentagem_menor = models.IntegerField()
    valor_minimo = models.FloatField(max_length=20)
    porcentagem_maior = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return 'Plano {} - {}%'.format(self.valor_minimo, self.porcentagem_maior)

# Model para Vendedor    
class Vendedor(models.Model):
    nome = models.CharField(max_length=30)
    cep = models.IntegerField()
    logradouro = models.CharField(max_length=200)
    numero_casa = models.CharField(max_length=10)
    bairro = models.CharField(max_length=10)
    cidade = models.CharField(max_length=10)
    estado = models.CharField(max_length=10)
    telefone = models.CharField(max_length=20)
    idade = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    cpf = models.CharField(max_length=11)
    plano_de_comissoes = models.ForeignKey(PlanoComissoes, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nome

# Model para Vendas
class Venda(models.Model):
    MESES = (
        ('1', 'Janeiro'),
        ('2', 'Fevereiro'),
        ('3', 'Março'),
        ('4', 'Abril'),
        ('5', 'Maio'),
        ('6', 'Junho'),
        ('7', 'Julho'),
        ('8', 'Agosto'),
        ('9', 'Setembro'),
        ('10', 'Outubro'),
        ('11', 'Novembro'),
        ('12', 'Dezembro'),
    )
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    mes = models.CharField(choices=MESES, max_length=2)
    ano = models.CharField(max_length=4)
    valor_vendas = models.FloatField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
       return 'Vendas {}/{}'.format(self.mes, self.ano)
