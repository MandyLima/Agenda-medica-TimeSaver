CREATE TABLE IF NOT EXISTS "usuario" (
    "id"        INTEGER NOT NULL,
    "nm_usuario"     TEXT NOT NULL UNIQUE,
    "senha_hash"  TEXT NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "consulta" (
    "id"                INTEGER NOT NULL,
    "nm_paciente"       TEXT NOT NULL,
    "cpf_paciente"      TEXT NOT NULL,
    "nm_medico"         TEXT NOT NULL,
    "nm_especialidade"  TEXT NOT NULL,
    "dt_consulta"       TEXT NOT NULL,
    "hr_consulta"       TEXT NOT NULL,
    "nm_convenio"       TEXT,
    "status_consulta"   TEXT NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
);