def eh_expressao_valida(expressao: str) -> bool:
    expr = expressao.replace(" ", "")

    if not expr:
        return False
    operadores = {'+', '-', '*', '/'}
    # Regra 3: Não pode começar ou terminar com operador.
    if expr[0] in operadores or expr[-1] in operadores:
        return False
 
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

    return True