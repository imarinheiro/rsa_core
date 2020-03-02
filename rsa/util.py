# coding: utf-8

def is_relative_prime(a, b):
    """Retorna ``True`` se ``a`` e ``b`` forem relativamente numeros primos.
    Dois numeros são relativamente primos se não compatilharem fatores comuns,
    ou seja, nao ha um numero inteiro (exceto 1) que divida ambos os numeros.
    """
    for n in range(2, min(a, b) + 1):
        if a % n == b % n == 0:
            return False
    return True
