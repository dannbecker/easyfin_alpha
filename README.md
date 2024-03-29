# EasyFin (Ver. Alpha)
### <span style="color:orange">Projeto descontinuado nessa linguagem</span>
#### Agora encontra-se no [repositório do front-end](https://github.com/arthurrivas/spa-easy-fin) e no [repositório do back-end](https://github.com/arthurrivas/api-easy_fyn).
**[PT-BR]**
O projeto consiste na elaboração de um website para cadastro de alunos e professores para visualização de notícias e cadastramento de questões. O projeto encontra-se em desenvolvimento, feito em Python utilizando o **Flask** no backend e bootstrap, jquery e javascript no frontend. O banco de dados utilizado é o SQLite.<br>
* O CRUD já está funcional;<br>
* A utilização de Fetch API também está funcional;<br>
* Realizar uma sessão é possível;<br>
* Existe a verificação de excessões e erros;<br>

# Requirements:

Python version needed: at least **Python 3**
Python version used: 3.9.2

pip and virtualenv

### Packages to install:

```
pip install Flask
pip install Flask-Login
pip install Flask-Migrate
pip install Flask-Script
pip install Flask-SQLAlchemy
pip install Flask-WTF
pip install SQLAlchemy
pip install WTForms
pip install WTForms[email]
```
### Packages:
```
alembic==1.5.6
click==7.1.2
dnspython==2.1.0
email-validator==1.1.2
Flask==1.1.2
Flask-Login==0.5.0
Flask-Migrate==2.7.0
Flask-Script==2.0.6
Flask-SQLAlchemy==2.4.4
Flask-WTF==0.14.3
idna==3.1
itsdangerous==1.1.0
Jinja2==2.11.3
Mako==1.1.4
MarkupSafe==1.1.1
python-dateutil==2.8.1
python-editor==1.0.4
six==1.15.0
SQLAlchemy==1.3.23
Werkzeug==1.0.1
WTForms==2.3.3
```

# Commands:

Run server:<br>
```
python run.py runserver
```
Create a database:<br>
```
python run.py db init
```
Migrate current database:<br>
```
python run.py db migrate
```
Update current databases:<br>
```
python run.py db upgrade
```
# Step-by-step guide:

**[PT-BR]**

### Passo 1. Instalar o Python

* Vá para <a href="https://www.python.org/downloads/">website do Python e instale a versão 3 ou superior.</a>
* Durante a instalação, lembre-se de adicionar o Python ao PATH.


### Passo 2. Instalar e preparar um ambiente virtual

* Com o Python instalado, abra o prompt de comando do seu sistema operacional e<a href="https://pip.pypa.io/en/stable/installing/"> siga estes passos (para instalar o pip).</a>

* Após instalado o pip, é possível instalar o virtualenv com o seguinte comando:

```
pip install virtualenv
```

* Agora, abra o prompt de comando dentro da pasta onde foi adicionado este repositório.
* Execute o seguinte comando:
```
virtualenv [nome-do-ambiente-virtual]
```
* Exemplo:
```
virtualenv venv
```
* Agora, abra o prompt de comando dento da pasta: [nome-do-ambiente-virtual]>Scripts>
* Execute o arquivo activate
* Pronto, você está dentro do ambiente virtual e pode seguir para o próximo passo.

### Passo 3. Instalação dos pacotes obrigatórios

* Dentro do ambiente virtual, comece a instalar os <a href="#packages-to-install">pacotes obrigatórios</a> conforme o exemplo:
```
pip install Flask
```

### Passo 4. Executando a aplicação

* Finalmente, na pasta raiz onde encontra-se o arquivo run.py, execute o seguinte comando:
```
python run.py runserver
```
* Pronto! A aplicação está sendo executada.
* Os <a href="#commands">demais comandos</a> são para o banco de dados.

