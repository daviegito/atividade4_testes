import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from src.validador_expressao import eh_expressao_valida

def test_deveRejeitarSeComecarOuTerminarComOperador():
    casos_invalidos = ["+1", "1*", "/"]
    for expr in casos_invalidos:
        assert eh_expressao_valida(expr) is False
