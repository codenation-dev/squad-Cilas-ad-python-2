# django-televendas
Projeto Final da Aceleração Python para Web realizado pela Codenation  
[Descrição do Projeto](README_CODENATION.md)  

### INSTALL  
- Clone o repositório.  
`git clone https://github.com/codenation-dev/squad-4-ad-python-2.git`  
`cd squad-4-ad-python-2`  
- Instale as dependências.  
`pip install -r requeriments.txt`  
- Construa o banco de dados.  
`cd codenation`  
`python manager.py migrate`  
- Carregue os dados de exemplo  
`python manage.py loaddata televendas.json`  
- rode o servidor.  
`python manage.py runserver`  

Recomendável criar um ambiente virtual de desenvolvimento.  
`python -m venv venv`  

