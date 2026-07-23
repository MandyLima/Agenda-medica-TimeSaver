import os
import tempfile
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app as flask_app
import db
from werkzeug.security import generate_password_hash


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()
    flask_app.config.update({"TESTING": True, "DATABASE": db_path})

    with flask_app.app_context():
        db.init_db()
        conn = db.get_db()
        conn.execute(
            "INSERT INTO usuario (nm_usuario, senha_hash) VALUES (?, ?)",
            ("usuario_teste", generate_password_hash("senha_teste"))
        )
        conn.commit()

    yield flask_app  

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()