from flask import Flask, make_response, jsonify
import db
from views import bp

app = Flask(__name__, instance_relative_config=True)

app.config.from_mapping(
    SECRET_KEY='secret',
    DATABASE=app.instance_path + '/agenda.sqlite',
)
db.init_app(app)

app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True)