from flask import Blueprint, make_response, jsonify
from api import Consultas

bp = Blueprint('views', __name__)

#rotas
@bp.route("/")
def homepage():
    return "Hello, World!"

@bp.route('/consultas', methods=['GET'])
def get_consultas():
    return make_response(
       jsonify(Consultas),200
    )