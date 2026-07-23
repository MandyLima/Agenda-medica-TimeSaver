#!/bin/bash
set -e

cd /agenda

if [ ! -f "instance/agenda.db" ]; then
    echo "Banco de dados não encontrado. Inicializando..."
    python -c "
from main import app
import db
with app.app_context():
    db.init_db()
"
fi

python database/seed.py

exec "$@"