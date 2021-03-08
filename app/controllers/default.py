from app import app, db
from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user
from app.models.forms import loginForm
from app.models.tables import Aluno, Professor

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/indexV2")
def index2():
    return render_template('index_v2.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    form = loginForm()

    if form.validate_on_submit():
        aluno = Aluno.query.filter_by(email=form.email.data).first()
        if aluno and aluno.password == form.password.data:
            login_user(aluno)
            return redirect(url_for("dashboard"))
        else:
            flash("E-mail e/ou senha inválidos.")
    else: 
        print(form.errors)
    return render_template('log-in.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/temp")
def homebase():
    return render_template('temp.html')


@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste(info):
    aluno = Aluno.query.filter_by(email="daniel@teste.com").first()
    print(aluno.nome, aluno.password)
    return aluno.nome


@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')


@app.route("/perfil/<user>")
def perfil(user):
    return render_template('perfil.html')


@app.route("/alunos")
def alunos():
    return render_template('alunos.html')


@app.route("/professores")
def professores():
    return render_template('professores.html')


@app.route("/noticias")
def noticias():
    return render_template('noticias.html')

@app.route("/configuracoes")
def configuracoes():
    return render_template('configuracoes.html')