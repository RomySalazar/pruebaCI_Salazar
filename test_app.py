# test_app.py
from app import suma

def test_suma():
    # Esta es una aserción: verifica que la suma de 2 y 3 sea igual a 5
    assert suma(2, 3) == 5
