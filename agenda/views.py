from flask import Blueprint

bp = Blueprint('views', __name__)

#rotas
@bp.route("/")
def homepage():
    return "Hello, World!"