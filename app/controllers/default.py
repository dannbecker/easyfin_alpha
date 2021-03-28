from app import app, db
from flask import render_template, flash, redirect, request, url_for, jsonify, g
from flask_login import login_user, logout_user
from app.models.forms import loginForm, validatePassword, addEscola, removeEscola, addAluno, removeAluno, addProfessor, removeProfessor
from app.models.tables import Aluno, Professor, Escola

@app.route("/home")
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


@app.route("/temp", methods=["POST", "GET", "DELETE"])
def temp():
    return render_template('temp.html' )

# TESTE # # TESTE # # TESTE # # TESTE # # TESTE # # TESTE # # TESTE # # TESTE # # TESTE #
@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste(info):
    aluno = Aluno.query.filter_by(email="daniel@teste.com").first()
    print(aluno.nome, aluno.password)
    return "Ok"
# TESTE # # TESTE # # TESTE # # TESTE # # TESTE # # TESTE # # TESTE # # TESTE # # TESTE #

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')


@app.route("/perfil/<user>")
def perfil(user):
    return render_template('perfil.html')


@app.route("/alunos", methods=["POST", "GET"])
def alunos():
    form = addAluno()
    if form.validate_on_submit():
        aluno = Aluno(form.email.data, form.nome.data, form.sobrenome.data, form.password.data)
        if aluno:
            db.session.add(aluno)
            db.session.commit()
            print(aluno)
            return redirect(url_for("alunos"))

    alunos = Aluno.query.all()

    return render_template('alunos.html', alunos=alunos, form=form)

@app.route("/remover/alunos", methods=["POST", "GET", "DELETE"])
def rmvAlunos():

    alunos = Aluno.query.all()
    form_rmv = removeAluno()
    if form_rmv.validate_on_submit():
        aluno = Aluno.query.filter_by(email=form_rmv.email.data).first()
        if aluno:
            db.session.delete(aluno)   
            db.session.commit()
            print("Aluno deletado!")
            return redirect(url_for("rmvAlunos"))
        else:
            flash("E-mail não encontrado no banco de dados!")
            print(aluno)
    

    return render_template('remover-aluno.html', alunos=alunos, form_rmv=form_rmv)


@app.route("/professores", methods=["POST", "GET"])
def professores():
    form = addProfessor()
    if form.validate_on_submit():
        professor = Professor(form.email.data, form.nome.data, form.sobrenome.data, form.password.data, form.disciplina.data)
        if professor:
            db.session.add(professor)
            db.session.commit()
            print(professor)
            return redirect(url_for("professores"))

    professores = Professor.query.all()

    return render_template('professores.html', professores=professores, form=form)


@app.route("/noticias", methods=["POST", "GET"])
def noticias():
    return render_template('noticias.html')


@app.route("/questoes", methods=["POST", "GET"])
def questoes():
    return render_template('questoes.html')


@app.route("/configuracoes", methods=["POST", "GET"])
def configuracoes():
    return render_template('configuracoes.html')


@app.route("/escolas", methods=["POST", "GET", "DELETE"])
def escolas():
    form = addEscola()
    if form.validate_on_submit():
        escola = Escola(form.cep.data, form.nome.data, form.rua.data, form.numero.data, 
        form.complemento.data, form.bairro.data, form.cidade.data, form.estado.data)
        if escola:
            db.session.add(escola)
            db.session.commit()
            return redirect(url_for("escolas"))
        else:
            print(form.errors)
    
    escolas = Escola.query.all()

    form_rmv = removeEscola()
    if form_rmv.validate_on_submit():
        escola = Escola.query.filter_by(nome=form_rmv.nome.data).first()
        if escola:
            db.session.delete(escola)   
            db.session.commit()
            print("Escola deletada!")
            return redirect(url_for("escolas"))
        else:
            flash("Nome não encontrado no banco de dados!")
    

    return render_template('escolas.html', form=form, escolas=escolas, form_rmv=form_rmv)


@app.route("/not_found")
def notfound():
    return render_template('not_found.html')


@app.route('/logged-base', methods=['GET', 'POST'])
def test():
    return render_template('logged-base.html')


@app.route('/apagar/professor/<int:id>', methods=['POST','GET'])
def apagar_professor(id):
    professor = Professor.query.filter_by(id=id).first()
    db.session.delete(professor)
    db.session.commit()


    return redirect(url_for("professores"))

@app.route('/apagar/aluno/<int:id>')
def apagar_aluno(id):
    aluno = Aluno.query.filter_by(id=id).first()
    db.session.delete(aluno)
    db.session.commit()

    return redirect(url_for("alunos"))

@app.route('/apagar/escola/<int:id>')
def apagar_escola(id):
    escola = Escola.query.filter_by(id=id).first()
    db.session.delete(escola)
    db.session.commit()

    return redirect(url_for("escolas"))