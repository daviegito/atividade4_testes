from src.ehExpressaoValida import ehExpressaoValida

def test_deveAceitarNumeroUnico():
    assert ehExpressaoValida(5) == True
