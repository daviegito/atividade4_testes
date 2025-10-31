def validador_expressao(expressao):

    # ciclo 1 - tipo inválido
    if expressao is None:
        return False
    
    # converte tudo pra string (caso número passe direto)
    if isinstance(expressao, int):
        return True

    # ciclo 2 - regra 6
    expr = expressao.replace(" ", "")
    if not expr:
        return False

    # ciclo 3 – número único válido
    if expr.isdigit():
        return True

    # ciclo 4 – regra 3
    operadores = {"+", "-", "*", "/"}
    if expr[0] in operadores or expr[-1] in operadores:
        return False
    
    # ciclo 6 - regra 1
    balanceamento = 0
    for char in expr:
        if char == '(':
            balanceamento += 1
        elif char == ')':
            balanceamento -= 1

        if balanceamento < 0:
            return False
    if balanceamento != 0:
        return False

    # demais casos ainda não implementados (ciclos 5+)
    return False