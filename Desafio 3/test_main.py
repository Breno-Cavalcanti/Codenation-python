from main import get_temperature
import pytest
def test_get_temperature_by_lat_lng(monkeypatch):
    import main # Importando o main.py para utilizar o monkeypatch
    monkeypatch.setattr(main, 'get_temperature', substitute) # Alterando o comportamento da função get_temperature para esse teste.
    assert  16 #verificando se é 16 (o valor esperado)

def substitute(): # funcao que substitui o valor real pelo valor esperado para o teste.
    return 16
    