def ehExpressaoValida(expressao):
    # remoção de espaços da expressão
    expr_sem_espaco = expressao.replace(" ", "")

    # se após remover os espaços a string estiver vazia, tem que retornar falso
    if expr_sem_espaco == "":
        return False

    # retorne falso pra qualquer outra expressão
    return False
