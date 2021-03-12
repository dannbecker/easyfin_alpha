# easyfin_alpha
[PT-BR]
O projeto consiste na elaboração de um website para cadastro de alunos e professores para visualização de notícia e cadastramento de questões.
O projeto está em desenvolvimento, desenvolvido em Python utilizando o Flask no backend, bootstrap, jquery e javascript no frontend.
O CRUD já está funcional. A utilização de Fetch API também está funcional.
Realizar uma sessão é possível.
Existe a verificação de excessões e erros.

# Requirements:

Python version needed: at least Python 3
Python version used: 3.9.2

pip and virtualenv

Packages:
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

# Commands:

Run server:
python run.py runserver

Create a database:
python run.py db init

Migrate current database:
python run.py db migrate

Update current databases:
python run.py db upgrade
