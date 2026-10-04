import sys


def buscar_usuario():
    return 'usuário do banco'


def saudacao():
    usuario = buscar_usuario()
    return f'Olá, {usuario}!'


def test_saudacao(monkeypatch):

    def buscar_usuario_fake():
        return 'Guilherme'

    monkeypatch.setattr(sys.modules[__name__], 'buscar_usuario', buscar_usuario_fake)

    assert saudacao() == 'Olá, Guilherme!'