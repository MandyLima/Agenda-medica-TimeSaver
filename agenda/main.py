from flask import Flask

app = Flask(__name__)

# Adicione o ponto (.) antes de views:
from views import bp
app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True)