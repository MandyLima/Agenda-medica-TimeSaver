from flask import Blueprint
from api import Consultas

bp = Blueprint('views', __name__)

#rotas
@bp.route("/")
def homepage():
    return "Hello, World!"

@app.route('/consultas', methods=['GET'])
def get_consultas():
    return make_response(
       jsonify(Consultas) 
    )
app.run()