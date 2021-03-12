from flask_wtf import FlaskForm  
from wtforms import StringField, PasswordField, BooleanField, SelectField, FieldList
from wtforms.validators import DataRequired, Email, EqualTo


class loginForm(FlaskForm):
    email = StringField("email", validators=[DataRequired(), Email(message="E-mail inválido.")])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")

class contactForm(FlaskForm):
    email = StringField("email", validators=[DataRequired(), Email(message="E-mail inválido.")])
    message = StringField("message", validators=[DataRequired()])

class addAluno(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])
    sobrenome = StringField("nome", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired(), Email(message="E-mail inválido.")])
    password = PasswordField("password", validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password', validators=[DataRequired()])
class removeAluno(FlaskForm):
    email = StringField("email", validators=[DataRequired()])

class addEscola(FlaskForm):
    cep = StringField("cep", validators=[DataRequired()])
    nome = StringField("nome", validators=[DataRequired()])
    rua = StringField("rua", validators=[DataRequired()])
    numero = StringField("numero", validators=[DataRequired()])
    complemento = StringField("complemento")
    bairro = StringField("bairro", validators=[DataRequired()])
    cidade = StringField("cidade", validators=[DataRequired()])
    estado = StringField("estado", validators=[DataRequired()])

class removeEscola(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])

class validatePassword(FlaskForm):
    password = PasswordField("password", validators=[DataRequired()])