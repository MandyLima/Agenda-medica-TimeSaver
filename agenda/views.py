from flask import Blueprint, make_response, jsonify, render_template, request, redirect, session, url_for
from werkzeug.security import check_password_hash
from api import Consultas
import db,requests,logging, sqlite3

bp = Blueprint('views', __name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

CAMPOS_OBRIGATORIOS = ['nome_paciente', 'cpf_paciente', 'nome_medico', 'especialidade_medico', 'data_consulta', 'hora_consulta', 'status']

#rotas
@bp.route("/")
def homepage():
    if 'user_id' not in session:
        return redirect(url_for('views.login'))
    return f"Bem-vindo, {session['username']}!"

@bp.route('/consultas', methods=['GET'])
def get_consultas():
    return make_response(
       jsonify(Consultas),200
    )

def validar_consultas(dados):
    validados = []
    for i, c in enumerate(dados):
        faltando = [campo for campo in CAMPOS_OBRIGATORIOS if not c.get(campo)]
        if faltando:
            logger.warning(f"Registro {i} (id={c.get('id', '?')}) com campos obrigatórios ausentes: {faltando}")
        for campo in CAMPOS_OBRIGATORIOS:
            c.setdefault(campo, "N/A")
        validados.append(c)
    return validados

@bp.route('/agenda')
def agenda():
    if 'user_id' not in session:
        return redirect(url_for('views.login'))
    username = session.get('username', 'Usuário')
    try:
        url = url_for('views.get_consultas', _external=True)
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()
        dados = validar_consultas(dados)
        
        if not dados:
            return render_template('agenda.html', consultas=[], erro="Nenhum agendamento encontrado.", usuario=username)

        return render_template('agenda.html', consultas=dados, erro=None, usuario=username)
    
    except requests.exceptions.ConnectionError:
        return render_template('agenda.html', consultas=[], erro="Não foi possível conectar à API de agendamentos.", usuario=username)
    except requests.exceptions.Timeout:
        return render_template('agenda.html', consultas=[], erro="A API demorou demais para responder.", usuario=username)
    except requests.exceptions.RequestException as e:
        return render_template('agenda.html', consultas=[], erro=f"Erro ao buscar agendamentos: {e}", usuario=username)
    
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method =="GET":
        return render_template('login.html')
    elif request.method =="POST":
        username = request.form.get('username')
        password = request.form.get('password')
    try:
        con = db.get_db()
        usuario = con.execute(
            'SELECT * FROM usuario WHERE nm_usuario = ?',
            (username,)
        ).fetchone()
    except sqlite3.Error as e:
        logger.error(f"Erro de banco de dados no login: {e}")
        return render_template('login.html', erro="Erro ao acessar o sistema. Tente novamente mais tarde."), 500

    if usuario is None or not check_password_hash(usuario['senha_hash'], password):            
        return render_template('login.html', erro="Usuário ou senha incorretos"), 401

    session['user_id'] = usuario['id']
    session['username'] = usuario['nm_usuario']
    return redirect (url_for('views.agenda')) 

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('views.login'))