def test_login_com_senha_errada_retorna_401(client):
    resposta = client.post('/login', data={
        'username': 'usuario_teste',
        'password': 'senha_errada'
    })
    assert resposta.status_code == 401


def test_acessar_agenda_sem_login_redireciona(client):
    resposta = client.get('/agenda')
    assert resposta.status_code == 302