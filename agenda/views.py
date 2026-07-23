from flask import Blueprint, make_response, jsonify, render_template, request, redirect, session, url_for
from werkzeug.security import check_password_hash
from api import Consultas
import db

bp = Blueprint('views', __name__)

#rotas
@bp.route("/")
def homepage():
    if 'user_id' not in session:
        return redirect(url_for('views.login'))
    return f"Bem-vindo, {session['username']}! (agenda vem aqui)"

@bp.route('/consultas', methods=['GET'])
def get_consultas():
    return make_response(
       jsonify(Consultas),200
    )

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method =="GET":
        return render_template('login.html')
    elif request.method =="POST":
        username = request.form.get('username')
        password = request.form.get('password')

        con = db.get_db()
        usuario = con.execute(
            'SELECT * FROM usuario WHERE nm_usuario = ?',
            (username,)
        ).fetchone()
    if usuario is None or not check_password_hash(usuario['senha_hash'], password):            
        return "Usuário ou senha incorretos", 401

    session['user_id'] = usuario['id']
    session['username'] = usuario['nm_usuario']
    return redirect (url_for('views.homepage')) 