DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True


# Criptografia dos formulários
SECRET_KEY = 'temp_password'

# Importar arquivos

UPLOAD_PERFIL_IMAGE = "app\static\img\perfil"
PERFIL_ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}