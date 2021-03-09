from app import db, login_manager

@login_manager.user_loader
def load_user(id):
    return Professor.query.filter_by(id=id).first()

class Aluno(db.Model):
    __tablename__ = "alunos"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    nome = db.Column(db.String)
    sobrenome = db.Column(db.String)
    password = db.Column(db.String)

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, email, nome, sobrenome, password):
        self.email = email
        self.nome = nome
        self.sobrenome = sobrenome
        self.password = password
    
    def __repr__(self):
        return "<Aluno %r>" % self.nome
    
class Professor(db.Model):
    __tablename__ = "professores"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    nome = db.Column(db.String)
    sobrenome = db.Column(db.String)
    password = db.Column(db.String)
    disciplina = db.Column(db.String)

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, email, nome, sobrenome, password, disciplina):
        self.email = email
        self.nome = nome
        self.sobrenome = sobrenome
        self.password = password
        self.disciplina = disciplina
    
    def __repr__(self):
        return "<Professor %r>" % self.nome


class Escola(db.Model):
    __tablename__ = "escolas"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    cep = db.Column(db.String)
    rua = db.Column(db.String)
    numero = db.Column(db.String)
    complemento = db.Column(db.String)
    bairro = db.Column(db.String)
    cidade = db.Column(db.String)
    estado = db.Column(db.String)

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, nome, cep, rua, numero, complemento, bairro, cidade, estado):
        self.nome = nome
        self.cep = cep
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado        
    
    def __repr__(self):
        return "<Escola %r>" % self.nome





"""class Pessoa(db.Model):
    __tablename__ = "pessoas"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    nome = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, email, nome, password):
        self.email = email
        self.nome = nome
        self.password = password
    
    def __rpr__(self):
        return "<Pessoa: %r>" % self.nome


class Turma(db.Model):
     __tablename__ = "pessoas"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)

    def __init__(self, nome):
        self.nome = nome
    
    def __rpr__(self):
        return "<Turma: %r>" % self.nome


class Disciplina(db.Model):
     __tablename__ = "disciplinas"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)

    def __init__(self, nome):
        self.nome = nome
    
    def __rpr__(self):
        return "<Disciplina: %r>" % self.nome
    

class Assunto(db.Model):
     __tablename__ = "assuntos"

    id = db.Column(db.Integer, primary_key=True)
    id_disciplina = db.Column(db.Integer, db.ForeignKey('disciplinas.id'))
    nome = db.Column(db.String)

    disciplina = db.relationship('Disciplina', foreign_keys=id_disciplina)

    def __init__(self, nome):
        self.nome = nome
    
    def __rpr__(self):
        return "<Disciplina: %r>" % self.nome"""