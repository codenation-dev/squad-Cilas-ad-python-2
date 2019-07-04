# django-televendas
Projeto Final da Aceleração Python para Web realizado pela Codenation  
[Descrição do Projeto](README_CODENATION.md)  

### INSTALL  
- Clone o repositório.  
`git clone https://gitlab.com/cilas/django-televendas`  
`cd django-televendas`  
- Instale as dependências.  
`pip install -r requeriments.txt`  
- Construa o banco de dados.  
`cd codenation`  
`python manager.py migrate`  
- Carregue os dados de exemplo  
`python manage.py loaddata televendas.json`  
- rode o servidor.  
`python manage.py runserver`  

Recomendável isolar o ambiente de desenvolvimento.  
`python -m venv venv`  

### TODO  
- Cadastrar Vendedores
- Cadastrar plano de comissões
- Registrar vendas mensais
- Calcular comissão dos vendedores
- Recuperar lista de vendedores ordenados pelo valor da comissão
- Enviar notificação aos vendedores que estão com a média de comissão baixa nos últimos meses
