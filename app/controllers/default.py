from app import app, db
from flask import render_template, flash, redirect, request, url_for, jsonify
from flask_login import login_user, logout_user
from app.models.forms import loginForm, addEscola
from app.models.tables import Aluno, Professor, Escola

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
        global professor
        professor = Professor.query.filter_by(email=form.email.data).first()
        if professor and professor.password == form.password.data:
            login_user(professor)
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


@app.route("/alunos", methods=["POST", "GET"])
def alunos():
    return render_template('alunos.html')


@app.route("/professores", methods=["POST", "GET"])
def professores():
    return render_template('professores.html')


@app.route("/noticias", methods=["POST", "GET"])
def noticias():
    return render_template('noticias.html')


@app.route("/questoes", methods=["POST", "GET"])
def questoes():
    return render_template('questoes.html')


@app.route("/configuracoes", methods=["POST", "GET"])
def configuracoes():
    return render_template('configuracoes.html')


@app.route("/escolas", methods=["POST", "GET"])
def escolas():
    form = addEscola()
    if form.validate_on_submit():
        escola = Escola(form.cep.data, form.nome.data, form.rua.data, form.numero.data, 
        form.complemento.data, form.bairro.data, form.cidade.data, form.estado.data)
        db.session.add(escola)
        db.session.commit()
    else:
        print(form.errors)
    return render_template('escolas.html', form=form)


@app.route("/not_found")
def notfound():
    return render_template('not_found.html')


@app.route('/logged-base', methods=['GET', 'POST'])
def test():
    return render_template('logged-base.html')