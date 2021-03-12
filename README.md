# EasyFin (Ver. Alpha)
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
alembic==1.5.6<br>
click==7.1.2<br>
dnspython==2.1.0<br>
email-validator==1.1.2<br>
Flask==1.1.2<br>
Flask-Login==0.5.0<br>
Flask-Migrate==2.7.0<br>
Flask-Script==2.0.6<br>
Flask-SQLAlchemy==2.4.4<br>
Flask-WTF==0.14.3<br>
idna==3.1<br>
itsdangerous==1.1.0<br>
Jinja2==2.11.3<br>
Mako==1.1.4<br>
MarkupSafe==1.1.1<br>
python-dateutil==2.8.1<br>
python-editor==1.0.4<br>
six==1.15.0<br>
SQLAlchemy==1.3.23<br>
Werkzeug==1.0.1<br>
WTForms==2.3.3<br>

# Commands:

Run server:<br>
python run.py runserver<br>

Create a database:<br>
python run.py db init<br>

Migrate current database:<br>
python run.py db migrate<br>

Update current databases:<br>
python run.py db upgrade<br>
