# coding: utf-8


def is_relatively_prime(a, b):
    """
    Retorna ``True`` se ``a`` e ``b`` forem relativamente números primos.
    Dois numeros são relativamente primos se não compatilharem fatores comuns,
    ou seja, nao ha um numero inteiro (exceto 1) que divida ambos os numeros.

    :param a: primo inteiro a ser verificado
    :param b: primo inteiro a ser verificado a correlação
    :return: boolean indicando se é relativamente primo
    """
    for n in range(2, min(a, b) + 1):
        if a % n == b % n == 0:
            return False
    return True


def transform_string_to_number(text: str):
    """
    Transforma o texto informado no parâmetro para seu inteiro correspondente.

    :param text: texto que deve ser convertido para número
    :return: número inteiro convertido a partir do parâmetro text
    """
    return ord(text)


def transform_number_to_string(number: int):
    """
    Transforma o número informado no parametro para seu texto original.

    :param number: número que deve ser convertido para string novamente
    :return: texto convertido a partir do parametro number
    """
    return chr(number)
