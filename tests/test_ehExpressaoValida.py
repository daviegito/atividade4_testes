from src.ehExpressaoValida import ehExpressaoValida


def test_deveRejeitarExpressaoVazia():
    assert ehExpressaoValida("") == False

def test_deveRejeitarParentesesDesbalanceados():
    casos_invalidos = ["(1+2", "1+2)", ")("]
    for expr in casos_invalidos:
        assert ehExpressaoValida(expr) == False
def test_deveRejeitarExpressaoApenasComEspacos():
    assert ehExpressaoValida(" ") == False

