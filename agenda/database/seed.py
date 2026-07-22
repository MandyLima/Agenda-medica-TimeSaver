import sqlite3
import os
from werkzeug.security import generate_password_hash

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "instance", "agenda.db")
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "schema.sql")

def criar_banco():
    os.makedirs(os.path.join(BASE_DIR, "instance"), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        conn.executescript(f.read())
    conn.commit()
    return conn

def inserir_usuario(conn):
    senha_hash = generate_password_hash("teste123")
    try:
        conn.execute(
            "INSERT INTO usuario (nm_usuario, senha_hash) VALUES (?, ?)",
            ("userteste", senha_hash)
        )
        conn.commit()
        print("Usuário de teste criado: username: userteste / senha: teste123")
    except sqlite3.IntegrityError:
        print("Usuário de teste já existe, ignorando.")
    
if __name__ == "__main__":
    conn = criar_banco()
    inserir_usuario(conn)
    conn.close()