from django.db import models
# Model Plano de Comissão
class PlanoComissoes(models.Model):
    descricao = models.CharField("Descrição", max_length=200)
    porcentagem_menor = models.IntegerField()
    valor_minimo = models.DecimalField(max_digits=8, decimal_places=2)
    porcentagem_maior = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return 'Plano {} - {}%'.format(self.valor_minimo, self.porcentagem_maior)

# Model para Vendedor    
class Vendedor(models.Model):
    nome = models.CharField("Nome", max_length=200)
    cep = models.IntegerField()
    logradouro = models.CharField("Logradouro", max_length=200)
    numero_casa = models.CharField("Número da Casa", max_length=50)
    bairro = models.CharField("Bairro", max_length=50)
    cidade = models.CharField("Cidade", max_length=50)
    estado = models.CharField("UF",max_length=2)
    telefone = models.CharField("Telefone", max_length=50)
    data_nascimento = models.DateField("Data de Nascimento")
    email = models.EmailField(max_length=254)
    cpf = models.CharField("CPF", max_length=11)
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
    mes = models.CharField("Mês", choices=MESES, max_length=2)
    ano = models.CharField("Ano", max_length=4)
    valor_vendas = models.DecimalField("Valor das Vendas", max_digits=8, decimal_places=2)
    valor_comissao = models.DecimalField("Valor da Comissão", max_digits=8, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
       return 'Vendas {}/{}'.format(self.mes, self.ano)
