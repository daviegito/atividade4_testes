from src.validador_expressao import validador_expressao

# ciclo 1
def test_deveRejeitarExpressaoVazia():
    assert validador_expressao("") is False

# ciclo 2
def test_deveRejeitarExpressaoApenasComEspacos():
    assert validador_expressao("") is False

# ciclo 3
def test_deveAceitarNumeroUnico():
    assert validador_expressao(5) is True

# ciclo 4
def test_deveRejeitarSeComecarOuTerminarComOperador():
    casos_invalidos = ["+1", "1*", "/"]
    for expr in casos_invalidos:
        assert validador_expressao(expr) is False

# ciclo 6
def test_deveRejeitarParentesesDesbalanceados():
    casos_invalidos = ["(1+2", "1+2)", ")("]
    for expr in casos_invalidos:
        assert validador_expressao(expr) is False
        