import os
import json
from collections import OrderedDict
from app import app, db
from flask import render_template, flash, redirect, request, url_for, jsonify, g
from flask_login import login_user, logout_user, current_user
from app.models.forms import loginForm, validatePassword, addEscola, removeEscola, addAluno, removeAluno, addProfessor, \
    removeProfessor
from app.models.tables import Aluno, Professor, Escola
from werkzeug.utils import secure_filename

@app.route("/temp", methods=["POST", "GET", "DELETE"])
def temp():
    professores = Professor.query.all()

    valores = {
        'nomes_completos': [],
        'emails': [],
    }

    for professor in professores:
        nome = Professor.get_name(professor)
        sobrenome = Professor.get_sobrenome(professor)
        email = Professor.get_email(professor)

        valores['nomes_completos'].append(nome + " " + sobrenome)
        valores['emails'].append(email)
        
    print(valores)
    jsonresult = jsonify({"professores": {
        'nomes_completos': valores['nomes_completos'],
        'emails': valores['emails']
    }})
    return jsonresult

#render_template('temp.html', professor=professores)

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

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['PERFIL_ALLOWED_EXTENSIONS']

def get_filepath():
    return os.path.abspath("app/static/img/perfil") + ("/")

def get_file_extension(file):
    filename_noext, file_extension = os.path.splitext(file.filename)
    return file_extension

def detect_image_path(image):
    filepath = get_filepath()
    image_path = filepath + image
    return os.path.isfile(image_path)

def detect_profile_picture():

    image = "id_" + (str(current_user.id) + ".jpg")
    src_path = "img/perfil/"
    if detect_image_path(image):
        return src_path + image
    else:
        return src_path + "default-avatar.jpg"

@app.route("/perfil/<user>")
def perfil(user):
    usuario = Aluno.query.filter_by(nome=user).first()
    foto_perfil = detect_profile_picture()

    return render_template('perfil.html', usuario=usuario, foto_perfil=foto_perfil)

@app.route("/perfil/<user>/upload-de-imagem", methods=['GET', 'POST'])
def perfil_upload_img(user):
    foto_perfil = detect_profile_picture()

    if request.method == 'POST':

        file = request.files['file']

        if get_file_extension(file) != ".jpg":
            flash('A imagem precisa estar no formato JPG.')
            return redirect(request.url)
      
        
        if file.filename == '':
            flash('Não foi selecionado uma imagem.')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filepath = get_filepath()
            image = "id_" + (str(current_user.id) + ".jpg")

            new_filename = filepath + image
            old_filename = filepath + file.filename

            if detect_image_path(image):
                os.remove(new_filename)

            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_PERFIL_IMAGE'], filename))
            os.rename(old_filename, new_filename)

            return redirect(url_for('perfil',
                                    user=user))

    return render_template('perfil-upload-img.html', foto_perfil=foto_perfil)

    
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
        professor = Professor(form.email.data, form.nome.data, form.sobrenome.data, form.password.data,
                              form.disciplina.data)
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


@app.route('/apagar/professor/<int:id>', methods=["POST", "GET"])
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


@app.route('/editar/professor/<int:id>', methods=['GET', 'POST'])
def editar_professor(id):
    professor = db.session.query(Professor).get(id)
    form = addProfessor(obj=professor)
    
    if form.validate_on_submit():
        form.populate_obj(professor)
        db.session.add(professor)
        db.session.commit()
        return redirect('/professores')
        

    return render_template('/editar-professor.html', form=form, professor=professor)

@app.route('/editar/aluno/<int:id>', methods=['GET', 'POST'])
def editar_aluno(id):
    aluno = db.session.query(Aluno).get(id)
    form = addAluno(obj=aluno)
    
    if form.validate_on_submit():
        form.populate_obj(aluno)
        db.session.add(aluno)
        db.session.commit()
        return redirect('/alunos')
        

    return render_template('/editar-aluno.html', form=form, aluno=aluno)

@app.route("/json/emails", methods=["POST", "GET"])
def json_emails():

    professores = Professor.query.all()
    alunos = Aluno.query.all()

    lista_usuarios = []
    lista_professores = []
    lista_alunos = []

    for professor in professores:
        id_prof = Professor.get_id(professor)
        nome = Professor.get_nome(professor)
        sobrenome = Professor.get_sobrenome(professor)
        email = Professor.get_email(professor)
        disciplina = Professor.get_disciplina(professor)

        dict_professor = {
            'id': id_prof,
            'nome': nome,
            'sobrenome': sobrenome,
            'email': email,
            'disciplina': disciplina
        }
        lista_professores.append(dict_professor)
        
    for aluno in alunos:
        id_aluno = Aluno.get_id(aluno)
        nome = Aluno.get_nome(aluno)
        sobrenome = Aluno.get_sobrenome(aluno)
        email = Aluno.get_email(aluno)

        dict_aluno = {
            'id': id_aluno,
            'nome': nome,
            'sobrenome': sobrenome,
            'email': email

        }

        lista_alunos.append(dict_aluno) 


    return jsonify(Professores=lista_professores, Alunos=lista_alunos)
