from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
# Arquivo de configurações do BD
app.config.from_object('config')

db = SQLAlchemy(app)
# Declaro o tratamento de migração, recebe a aplicação e o banco de dados
migrate = Migrate(app, db)

# Manager para cuidar dos comendos para inicializar a aplicação
manager = Manager(app)
manager.add_command('db', MigrateCommand)
from app.controllers import default
