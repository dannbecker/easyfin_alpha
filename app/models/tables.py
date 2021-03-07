from app import db

    
class Alunos(db.Model):
    __tablename__ = "alunos"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    nome = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, email, nome, password):
        self.email = email
        self.nome = nome
        self.password = password
    
    def __rpr__(self):
        return "<Aluno %r>" % self.nome
    
class Professores(db.Model):
    __tablename__ = "professores"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    nome = db.Column(db.String)
    password = db.Column(db.String)
    disciplina = db.Column(db.String)

    def __init__(self, email, nome, password, disciplina):
        self.email = email
        self.nome = nome
        self.password = password
        self.disciplina = disciplina
    
    def __rpr__(self):
        return "<Professor %r>" % self.nome

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