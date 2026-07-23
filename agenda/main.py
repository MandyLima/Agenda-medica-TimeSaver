import os
from flask import Flask
import db
from views import bp

app = Flask(__name__, instance_relative_config=True)

app.config.from_mapping(
    SECRET_KEY=os.environ.get('SECRET_KEY', 'dev-fallback-nao-usar-em-producao'),
    DATABASE=app.instance_path + '/agenda.db',
)
db.init_app(app)
app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)