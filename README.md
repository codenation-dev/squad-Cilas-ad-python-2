# django-televendas
Projeto Final da Aceleração Python para Web realizado pela Codenation  
[Descrição do Projeto](README_CODENATION.md)  

# INSTALL  
- Clone o repositório.  
`git clone https://github.com/cilas/django-televendas.git`  
- Instale as depêndencias.  
`pip install -r requeriments.txt`  
- Construa o banco de dados.  
`python manager.py migrate`  
- Crie um super usuário.  
`python manage.py createsuperuser`  
- rode o servidor.  
`python manage.py runserver`  

# TODO  
- Cadastrar Vendedores
- Cadastrar plano de comissões
- Registrar vendas mensais
- Calcular comissão dos vendedores
- Recuperar lista de vendedores ordenados pelo valor da comissão
- Enviar notificação aos vendedores que estão com a média de comissão baixa nos últimos meses
