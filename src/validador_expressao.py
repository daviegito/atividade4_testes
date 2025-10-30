def eh_expressao_valida(expressao: str) -> bool:

    expr = expressao.replace(" ", "")
    if not expr:
        return False

    operadores = {"+", "-", "*", "/"}
    if expr[0] in operadores or expr[-1] in operadores:
        return False

    return True
