from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

app = Flask(__name__)
# Arquivo de configurações do BD
app.config.from_object('config')

db = SQLAlchemy(app)
# Declaro o tratamento de migração, recebe a aplicação e o banco de dados
migrate = Migrate(app, db)

# Manager para cuidar dos comandos para inicializar a aplicação
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Manager para cuidar de uma sessão de login
login_manager = LoginManager() 
login_manager.init_app(app)

app.config['JSON_SORT_KEYS'] = False

# Importação dos modelos de formulário e tabelas; Importação dos controllers padrões
from app.models import tables, forms
from app.controllers import default
