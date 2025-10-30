from src.ehExpressaoValida import ehExpressaoValida


def test_deveRejeitarExpressaoVazia():
    assert ehExpressaoValida("") == False


def test_deveRejeitarExpressaoApenasComEspacos():
    assert ehExpressaoValida(" ") == False
