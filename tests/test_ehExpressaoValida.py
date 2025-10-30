from src.ehExpressaoValida import ehExpressaoValida

def test_deveRejeitarExpressaoVazia():
    assert ehExpressaoValida("") == False
