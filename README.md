# Agenda Médica

Aplicação web de login e consulta de agendamentos médicos, desenvolvida como desafio técnico para a TimeSaver.

## Descrição

Após login (validado contra banco SQLite), o usuário visualiza os agendamentos em uma tabela interativa (Tabulator), com busca por paciente, CPF ou médico. Os dados vêm de uma requisição HTTP para um endpoint próprio (`/consultas`), que simula uma API externa.

## Tecnologias

Python 3.11, Flask, SQLite, Tabulator.js, Requests, Docker, Pytest.

## Como Executar

```bash
git clone <url-do-repositorio>
cd agenda
cp .env.example .env
docker compose up --build
```

Acesse: `http://localhost:5000/login`

O banco é criado e populado automaticamente na primeira execução.

## Credenciais de Teste
Usuário: userteste
Senha: teste123

## Uso

1. Faça login com as credenciais acima.
2. Veja os agendamentos na tabela.
3. Use o campo de busca para filtrar por paciente, CPF ou médico.
4. Clique em "Sair" para encerrar a sessão.

## Decisões Técnicas

- SQLite puro (sem ORM), para manter controle direto do SQL.
- API mockada roda no mesmo app (endpoint `/consultas`); a tela de agenda faz uma requisição HTTP real a ela.
- A tabela `consulta` existe no schema mas não é usada como cache — dados sempre vêm ao vivo da API.
- Falhas (login inválido, banco indisponível, API indisponível, dados ausentes) são tratadas com mensagens amigáveis e logadas no terminal.


## Testes

```bash
pytest tests/ -v
```

Cobre: login com senha incorreta (401) e acesso à agenda sem sessão ativa (redirecionamento).
