from flask_wtf import FlaskForm  
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email


class loginForm(FlaskForm):
    email = StringField("email", validators=[DataRequired(), Email(message="E-mail inválido.")])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")

class contactForm(FlaskForm):
    email = StringField("email", validators=[DataRequired(), Email(message="E-mail inválido.")])
    message = StringField("message", validators=[DataRequired()])